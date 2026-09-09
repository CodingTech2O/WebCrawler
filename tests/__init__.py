from test_fetch_url import check_fetch
from test_rate_limit import check_rate
from test_check_robots_txt import check_check_robots
from test_process_links import check_process
import time

start = time.perf_counter()

tests = {}

check_fetch(tests)
check_rate(tests)
check_check_robots(tests)
check_process(tests)

end = time.perf_counter() - start
print("Test | Result")
for key,value in tests.items():
    print(f"{key} | {value}")

print(f"Time Taken {round(start-end,2)} ms")

