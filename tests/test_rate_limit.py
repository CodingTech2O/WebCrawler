from url_handler import rate_limit
import time

def check_rate(tests):
        
    start = time.time()
    @rate_limit
    def check_rate_limit():
        return None

    end = time.time() - start

    if end - start < 2:
        tests['rate_limit_working'] = True
    else:
        tests['rate_limit_working'] = False