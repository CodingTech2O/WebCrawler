from url_handler import check_robots_txt

def check_check_robots(tests):
    try:
        check_robots_txt("https://amazon.com/")
        tests['check_robots_txt_working'] = True
    except:
        tests['check_robots_txt_working'] = False
