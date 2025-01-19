import asyncio
from datetime import time

class RateLimiter:
    def __init__(self, rate_per_second):
        self.rate_per_second = rate_per_second
        self._last_call = None

    async def wait(self):
        if self._last_call:
            elapsed = time.time() - self._last_call
            wait_time = max(0, (1 / self.rate_per_second) - elapsed)
            await asyncio.sleep(wait_time)
        self._last_call = time.time()
