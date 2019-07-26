# from benchmark_selenium import run_selenium_benchmark
from benchmark_splash import run_splash_benchmark
from selenium import webdriver

urls = open("urls.txt").readlines()
report = open("report.txt", "w")


def write_report(messages):
    for mesg in messages:
        report.write(mesg + "\n")


for url in urls:
    url = url.strip()
    # messages = run_selenium_benchmark(url=url, driver=webdriver.Chrome())
    # report.writelines(messages)
    messages = run_splash_benchmark(url)
    write_report(messages)
    print("*************************************************************")
    print("*************************************************************")
report.close()
