from urllib.request import urlopen
import datetime


def make_splash_request(url):
    start_time = datetime.datetime.now()
    html_content = urlopen(url).read()  # The url you want to open
    end_time = datetime.datetime.now()
    dt = end_time - start_time
    ms = dt.total_seconds() * 1000  # milliseconds
    return ms


def make_selenium_request(driver=None, url=None,):
    start_time = datetime.datetime.now()
    driver.get(url)
    html = driver.page_source
    end_time = datetime.datetime.now()
    dt = end_time - start_time
    ms = dt.total_seconds() * 1000  # milliseconds
    return ms


def round_number(num):
    return "{0:.3f}".format(num)
