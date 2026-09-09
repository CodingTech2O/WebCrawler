from url_handler import process_links, fetch_url

def check_process(tests):
    try:
        process_links(fetch_url("https://example.com/"),"https://example.com")
        tests['process_links_working'] = True
    except:
        tests['process_links_working'] = False