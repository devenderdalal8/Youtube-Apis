import time

class RateLimiter:
    def __init__(self, rate_per_second):
        self.interval = 1.0 / rate_per_second
        self.last_called = time.perf_counter()

    def wait(self):
        now = time.perf_counter()
        elapsed = now - self.last_called
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_called = time.perf_counter()
