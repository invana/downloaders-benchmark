from base import make_splash_request, round_number

TEST_PAGE_URL = "https://www.bing.com/search?q=artificial+intelligence"


def run_splash_benchmark(url):
    SPLASH_URL = "http://127.0.0.1:8050/render.json"
    messages = []

    messages.append("===================================")
    messages.append("Splash benchmark for url {}".format(url))
    url = "{}?url={}&html=1".format(SPLASH_URL, url)
    NUM_OF_ITERATIONS = 10
    iteration_results = []
    for i in range(0, NUM_OF_ITERATIONS):
        elapsed_time_ms = make_splash_request(url)
        iteration_results.append(elapsed_time_ms)
        messages.append("iteration :{} \t\t{} ms".format(i, round_number(elapsed_time_ms)))

    messages.append("Total time take is {} ms".format(
        round_number(sum(iteration_results))))
    messages.append("Average time taken is {} ms".format(
        round_number(
            sum(iteration_results) / NUM_OF_ITERATIONS)))
    messages.append("===================================")
    return messages

# run_splash_benchmark(TEST_PAGE_URL)
