from flask import Flask, redirect, url_for, render_template,send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, urljoin
from threading import Lock


class URLForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

with open(r"data/urls.json", "r") as f:
    data = json.load(f)

file_lock = Lock()
background_executor = ThreadPoolExecutor(max_workers=4)


def fetch_url(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    links = []

    for l in soup.find_all("a", href=True):
        links.append(urljoin(url, l.get("href")))

    domain = urlparse(url).netloc
    base = f"data/{domain}"

    os.makedirs(base, exist_ok=True)

    with file_lock:
        with open(f"{base}/processed.txt", "a", encoding="utf-8") as f:
            f.write(url + "\n")

    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_") or "index"
    filename = path.replace("?", "_").replace("&", "_")

    with open(f"{base}/{filename}.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    return links


def process_links(links, url):
    domain = urlparse(url).netloc
    base = f"data/{domain}"

    os.makedirs(base, exist_ok=True)

    processed_path = f"{base}/processed.txt"

    if os.path.exists(processed_path):
        with open(processed_path, "r", encoding="utf-8") as f:
            processed = set(f.read().splitlines())
    else:
        processed = set()

    pending = []

    for link in links:
        if link.startswith("#"):
            continue

        if urlparse(link).netloc != domain:
            continue

        if link not in processed:
            processed.add(link)
            pending.append(link)

    while pending:
        batch = pending[:25]
        pending = pending[25:]

        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [
                executor.submit(fetch_url, link)
                for link in batch
            ]

            for future in futures:
                try:
                    new_links = future.result()
                except Exception:
                    continue

                for link in new_links:
                    if link.startswith("#"):
                        continue

                    if urlparse(link).netloc != domain:
                        continue

                    if link not in processed:
                        processed.add(link)
                        pending.append(link)


@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()

    if form.validate_on_submit():
        url = form.url.data

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        domain = urlparse(url).netloc

        data[url] = domain

        with open(r"data/urls.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        links = fetch_url(url)

        background_executor.submit(
            process_links,
            links,
            url
        )

        return redirect(
            url_for(
                "processing",
                url=domain
            )
        )

    return render_template("index.html", form=form)


@app.route("/scraper/<path:url>")
def processing(url):
    base = f"data/{url}"

    if not os.path.exists(base):
        return "Crawler not found", 404

    processed = [
        file for file in os.listdir(base)
        if file.endswith(".html")
    ]

    processed.sort()

    if os.path.exists(f"{base}/processed.txt"):
        with open(f"{base}/processed.txt", "r", encoding="utf-8") as f:
            links = f.read().splitlines()
    else:
        links = []

    return render_template(
        "processing.html",
        processed=processed,
        links=links,
        url=url,
        zip=zip
    )

@app.route("/download/<path:url>/<filename>")
def download(url, filename):
    return send_from_directory(
        f"data/{url}",
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)