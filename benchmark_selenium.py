from base import make_selenium_request, round_number

TEST_PAGE_URL = "https://www.bing.com/search?q=artificial+intelligence"


def run_selenium_benchmark(url, driver=None):
    NUM_OF_ITERATIONS = 10
    iteration_results = []
    messages = []
    messages.append("===================================")
    messages.append("Selenium benchmark for url {} with driver {}".format(url, driver))

    for i in range(0, NUM_OF_ITERATIONS):
        elapsed_time_ms = make_selenium_request(driver=driver, url=url)
        iteration_results.append(elapsed_time_ms)
        messages.append("iteration :{} \t\t{} ms".format(i, round_number(elapsed_time_ms)))

    driver.quit()
    messages.append("Total time take is {} ms".format(
        round_number(sum(iteration_results))))
    messages.append("Average time taken is {} ms".format(
        round_number(
            sum(iteration_results) / NUM_OF_ITERATIONS)))
    messages.append("===================================")
    return messages


# run_selenium_benchmark(TEST_PAGE_URL, driver=webdriver.Chrome())
