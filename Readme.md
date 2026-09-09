
# 🕷️ WebCrawler

A full-featured web crawler built with **Python, Flask, Requests, BeautifulSoup, and ThreadPoolExecutor**.

WebCrawler recursively explores websites, discovers internal links, downloads page content, and provides a web-based interface for managing and monitoring the crawling process.

---

## ✨ Features

- 🕷️ Recursive website crawling
- 🔗 Automatic internal-link discovery
- 🌐 Flask web interface
- ⚡ Concurrent URL processing with `ThreadPoolExecutor`
- 🍲 HTML parsing with BeautifulSoup
- 📡 HTTP requests using Requests
- 🔒 Thread-safe file operations
- 💾 Local storage of crawled data
- 📋 URL tracking and processing
- 🗂️ Organized project structure
- 🧪 Dedicated testing directory
- 🎨 Custom frontend using HTML/CSS
- 🌍 Restricts crawling to the target website/domain

---

## 🧠 How It Works

WebCrawler follows a recursive crawling process:

```text
                     ┌─────────────────┐
                     │   Enter URL     │
                     └────────┬────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Fetch Web Page  │
                    └────────┬─────────┘
                             │
                             ▼
                   ┌───────────────────┐
                   │ Parse HTML using  │
                   │   BeautifulSoup   │
                   └─────────┬─────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Extract Links   │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Filter Internal URLs│
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Check Already Seen   │
                  │       URLs           │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ ThreadPoolExecutor   │
                  │ Fetches URLs         │
                  │ Concurrently         │
                  └──────────┬───────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Save Page Data  │
                    └────────┬────────┘
                             │
                             ▼
                       Repeat Process
````

---

## 🛠️ Tech Stack

| Technology           | Purpose                     |
| -------------------- | --------------------------- |
| 🐍 Python            | Core programming language   |
| 🌐 Flask             | Web application framework   |
| 📡 Requests          | HTTP requests               |
| 🍲 BeautifulSoup     | HTML parsing                |
| ⚡ ThreadPoolExecutor | Concurrent URL processing   |
| 🔗 urllib.parse      | URL parsing and joining     |
| 🔒 threading.Lock    | Thread-safe file operations |
| 📄 JSON              | Data storage                |
| 🎨 HTML/CSS          | Frontend interface          |

---

## 📁 Project Structure

```text
WebCrawler/
│
├── data/
│   └── Crawl data and URL information
│
├── static/
│   └── CSS and static frontend files
│
├── templates/
│   └── HTML templates
│
├── tests/
│   └── Test files
│
├── .gitignore
├── Readme.md
├── app.py
└── url_handler.py
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CodingTech2O/WebCrawler.git
```

### 2. Enter the Project Directory

```bash
cd WebCrawler
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

Install the required Python packages:

```bash
pip install flask flask-wtf requests beautifulsoup4 python-dotenv
```

Or, if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application will start on the local Flask server.

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🕷️ Starting a Crawl

1. Open the WebCrawler web interface.
2. Enter the URL you want to crawl.
3. Submit the URL.
4. The crawler starts processing the website.
5. Internal links are discovered automatically.
6. New URLs are processed recursively.
7. Crawled content is stored locally.

---

## ⚡ Concurrent Crawling

WebCrawler uses Python's `ThreadPoolExecutor` to process multiple URLs concurrently.

Instead of processing every page strictly one after another:

```text
URL 1 → finish
URL 2 → finish
URL 3 → finish
URL 4 → finish
```

the crawler can process multiple URLs at the same time:

```text
          ┌── URL 1 ──┐
          ├── URL 2 ──┤
START ────┼── URL 3 ──┼──── DONE
          └── URL 4 ──┘
```

This improves crawling performance when working with multiple pages.

---

## 🔗 URL Handling

The crawler uses Python's `urllib.parse` utilities to work with URLs.

The URL handling system is responsible for tasks such as:

* Parsing URLs
* Joining relative URLs
* Identifying domains
* Building complete URLs
* Filtering discovered links

This helps prevent the crawler from blindly following unrelated external websites.

---

## 🍲 HTML Parsing

WebCrawler uses **BeautifulSoup** to parse downloaded HTML.

The crawler can inspect HTML documents and extract links from elements such as:

```html
<a href="https://example.com/about">
    About
</a>
```

Discovered links are then passed back into the crawling system.

---

## 💾 Data Storage

Crawled information is stored locally inside the `data/` directory.

A typical structure can look like:

```text
data/
│
└── example.com/
    │
    ├── ...
    └── ...
```

Keeping crawl data inside a dedicated directory makes it easier to organize results from different websites.

---

## 🔒 Thread Safety

Because multiple worker threads can operate simultaneously, file operations need to be handled carefully.

The project uses Python's `Lock`:

```python
from threading import Lock

file_lock = Lock()
```

The lock helps prevent multiple threads from modifying shared files at the same time.

---

## 🌐 Flask Web Interface

The project uses Flask to provide a browser-based interface.

Instead of interacting with the crawler entirely through a command line, users can interact with it through a web application.

The frontend is organized using:

```text
templates/
static/
```

The `templates/` directory contains HTML pages while `static/` contains frontend assets such as CSS.

---

## 🧪 Testing

Tests are organized inside:

```text
tests/
```

To run the test suite when `pytest` is installed:

```bash
pytest
```

You can also run:

```bash
python -m pytest
```

---

## 🛡️ Responsible Crawling

Use WebCrawler responsibly.

Before crawling a website, make sure automated access is permitted.

Important considerations include:

* Respect `robots.txt`
* Respect website terms of service
* Avoid excessive requests
* Avoid unnecessary server load
* Respect rate limits
* Only crawl websites you are allowed to access

This project is intended for **learning, development, testing, and authorized crawling**.

---

## ⚠️ Current Limitations

WebCrawler is a learning-focused crawler and is not intended to compete with large-scale production crawling systems.

Some current limitations include:

* No distributed crawling
* No JavaScript browser rendering
* Limited retry handling
* No database-backed storage
* No advanced crawl scheduling
* No configurable crawl-depth system
* No advanced rate limiting
* Limited HTTP status monitoring
* No dedicated crawler queue system

---

## 🔮 Future Improvements

Possible improvements include:


* [ ] Add automatic retry handling
* [ ] Add HTTP status-code tracking
* [ ] Add crawl statistics
* [ ] Add a crawler dashboard
* [ ] Add SQLite/PostgreSQL support
* [ ] Export results to JSON
* [ ] Export results to CSV
* [ ] Add sitemap support
* [ ] Improve logging
* [ ] Add Docker support
* [ ] Add asynchronous crawling
* [ ] Add JavaScript rendering
* [ ] Add better test coverage
* [ ] Add configurable worker count

---

## 🧩 Main Components

### `app.py`

The main Flask application.

Responsible for:

* Starting the web server
* Handling web requests
* Connecting the frontend to the crawler
* Managing the crawling workflow

### `url_handler.py`

Handles URL-related crawling functionality.

Responsible for:

* URL processing
* Link discovery
* URL handling
* Crawling-related operations

### `templates/`

Contains the HTML templates used by the Flask application.

### `static/`

Contains frontend assets such as CSS.

### `data/`

Contains generated crawler data.

### `tests/`

Contains project tests.

---

## 📚 What This Project Demonstrates

This project was built to explore practical concepts in Python and web development, including:

* Python programming
* HTTP requests
* Web scraping
* HTML parsing
* URL parsing
* Recursive algorithms
* Multithreading
* Thread synchronization
* Flask development
* File handling
* JSON data
* Frontend/backend integration
* Software project organization
* Testing

---

## 🎯 Project Goals

The main goal of WebCrawler is to build a practical crawler while learning how different software components work together.

The project combines:

```text
Python
   +
HTTP
   +
HTML Parsing
   +
URL Processing
   +
Multithreading
   +
Flask
   +
File Storage
   =
WebCrawler
```

---

## 📈 Why Build a Web Crawler?

Building a crawler is a great way to understand how several important areas of computer science and software engineering work together.

It involves:

* Networking
* Data extraction
* Algorithms
* Concurrency
* File systems
* Web development
* Data processing

Rather than using an existing crawler framework, this project focuses on implementing the core crawling logic directly in Python.

---

## 👨‍💻 Author

### CodingTech2O

GitHub:

[https://github.com/CodingTech2O](https://github.com/CodingTech2O)

---

## 🤝 Contributing

Contributions and suggestions are welcome.

### Steps

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/my-feature
```

3. Make your changes.
4. Test your changes.
5. Commit your changes.

```bash
git commit -m "Add my feature"
```

6. Push your branch.

```bash
git push origin feature/my-feature
```

7. Open a Pull Request.

---

## ⭐ Support

If you found the project useful or interesting, consider giving the repository a ⭐ on GitHub.

Every star helps motivate further development.

---


# 🕷️ WebCrawler

**Built with Python. Powered by curiosity.**

> Crawl. Parse. Discover. Repeat.

