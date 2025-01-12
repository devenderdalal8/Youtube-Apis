import redis
import json

class RedisCache:
    def __init__(self, redis_url="redis://localhost", decode_responses=True):
        self.pool = redis.ConnectionPool.from_url(redis_url, decode_responses=decode_responses)
        self.redis = redis.StrictRedis(connection_pool=self.pool)

    def get(self, key):
        value = self.redis.get(key)
        if value:
            return json.loads(value)
        return None

    def set(self, key, value, expire=3600):
        self.redis.set(key, json.dumps(value), ex=expire)
