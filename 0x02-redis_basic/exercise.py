#!/usr/bin/env python3
import redis
import uuid
"""Create a Cache class. In the __init__ method, store an instance of Redis"""


class Cache:
    """class Cache"""
    def __init__(self):
        """constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | int | float | bytes) -> str:
        """method to set a value to the db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
