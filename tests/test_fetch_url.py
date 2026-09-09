from url_handler import fetch_url


def check_fetch(tests):
    try:
        fetch_url("https://example.com")
        tests['fetch_url_working'] = True
    except:
        tests['fetch_url_working'] = False