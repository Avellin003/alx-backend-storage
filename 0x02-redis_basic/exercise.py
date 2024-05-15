#!/usr/bin/env python3
"""Class that generates a key using redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    def __init__(self):
        # Initializes redis
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Creates a random
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        # Returns a key
        return key

    def get(self, key: str, fn: Callable = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def decode_utf8(self, value: bytes) -> str:
        return value.decode('utf-8')

    def get_str(self, key: str) -> str:
        return self.get(key, self.decode_utf8)

    def get_int(self, key: str) -> int:
        return self.get(key, int)


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


# Decorate Cache.store with count_calls
Cache.store = count_calls(Cache.store)
