import os
import requests #type:ignore
from bs4 import BeautifulSoup#type:ignore
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, urljoin
from threading import Lock

file_lock = Lock()



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
