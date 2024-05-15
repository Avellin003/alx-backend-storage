#!/usr/bin/env python3
"""Class that generates a key using redis"""
import redis
import uuid
from typing import Union, Callable


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
