from flask import Flask, redirect, url_for, render_template,send_from_directory #type:ignore
from flask_wtf import FlaskForm #type:ignore
from wtforms import StringField, SubmitField #type:ignore
from wtforms.validators import DataRequired #type:ignore
import os
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, urljoin
from threading import Lock
from url_handler import *


class URLForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

with open(r"data/urls.json", "r") as f:
    data = json.load(f)

background_executor = ThreadPoolExecutor(max_workers=4)



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
    app.run()