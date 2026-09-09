# 🕷️ WebCrawler

A full-stack Python web crawler built with **Flask, Requests, BeautifulSoup, and ThreadPoolExecutor**.

WebCrawler recursively explores a website, discovers internal links, downloads the HTML of each page, and provides a web interface for monitoring the crawling process.

## ✨ Features

* 🕷️ Recursive website crawling
* 🔗 Automatic internal-link discovery
* ⚡ Concurrent page fetching with `ThreadPoolExecutor`
* 🌐 Flask-based web interface
* 💾 Saves crawled HTML pages locally
* 📋 Tracks already processed URLs
* 🚫 Automatically ignores external domains
* 📁 Organizes crawled data by domain
* ⬇️ Allows downloaded HTML pages to be retrieved
* 🔐 URL form validation using Flask-WTF
* ⏱️ Request timeout protection

## 🛠️ Tech Stack

* **Python**
* **Flask** — Web framework
* **Requests** — HTTP requests
* **BeautifulSoup4** — HTML parsing
* **Flask-WTF / WTForms** — Form handling and validation
* **ThreadPoolExecutor** — Concurrent crawling
* **JSON** — URL metadata storage

## 📂 Project Structure

```text
WebCrawler/
│
├── app.py
│
├── data/
│   └── urls.json
│
├── static/
│   └── style.css
│   └── processing.css
│
├── templates/
│   └── index.html
│   └── processing.html
│
├── .env
└── README.md
```

When a website is crawled, its pages are stored inside:

```text
data/
└── example.com/
    ├── processed.txt
    ├── index.html
    ├── about.html
    └── ...
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/CodingTech2O/WebCrawler.git
cd WebCrawler
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-wtf wtforms requests beautifulsoup4 python-dotenv
```

### 4. Configure the secret key

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
```

### 5. Run the application

```bash
python app.py
```

The application will start locally. Open the address shown in your terminal in a browser.

## 🕸️ How It Works

The crawler follows this general pipeline:

```text
                ┌──────────────┐
                │ Enter URL    │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Fetch Page   │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Parse HTML   │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Find Links   │
                └──────┬───────┘
                       ↓
             ┌─────────┴─────────┐
             ↓                   ↓
       Internal Links       External Links
             ↓                   ↓
          Crawl                 Ignore
             ↓
      Save HTML + URL
             ↓
       Repeat Until Done
```

### Concurrency

The crawler uses Python's `ThreadPoolExecutor` to fetch multiple pages concurrently rather than processing every page sequentially.

This allows the crawler to spend less time waiting for network requests.

## 💾 Data Storage

For every crawled domain, WebCrawler creates a separate directory:

```text
data/<domain>/
```

Each successfully crawled page is saved as an HTML file.

A `processed.txt` file keeps track of URLs that have already been crawled, preventing unnecessary duplicate requests.

## ⚠️ Limitations

This project is primarily intended for learning and experimentation.

Current limitations include:

* JavaScript-rendered content is not supported
* No robots.txt handling yet
* No configurable crawl depth
* No rate limiting
* No retry/backoff system
* HTML filename collisions are possible for some complex URLs
* Crawling state is stored locally rather than in a database
* Error handling could be expanded

## 🔮 Future Improvements

Planned improvements could include:

* [ ] Crawl-depth configuration
* [ ] Robots.txt support
* [ ] Rate limiting
* [ ] Retry with exponential backoff
* [ ] Crawl statistics dashboard
* [ ] Pause/resume crawling
* [ ] Stop crawling button
* [ ] URL queue visualization
* [ ] SQLite/PostgreSQL storage
* [ ] Export results to JSON/CSV
* [ ] Better duplicate URL normalization
* [ ] Sitemap support
* [ ] JavaScript rendering with a browser engine
* [ ] Unit tests
* [ ] Docker support

## 🎯 Purpose

This project was built to explore:

* Web crawling
* HTTP requests
* HTML parsing
* URL handling
* Concurrency
* Flask web applications
* File-based data storage
* Background task execution

## ⚖️ Responsible Use

Only crawl websites where you have permission to do so or where crawling is permitted by the site's policies.

Avoid sending excessive requests to servers.

### ⭐ If you found this project interesting

Feel free to star the repository and experiment with the code!
