#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
"""Create a Cache class. In the __init__ method, store an instance of Redis"""

type my_union = Union[str, float, int, bytes]


class Cache:
    """class Cache"""
    def __init__(self):
        """constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: my_union) -> str:
        """method to set a value to the db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> my_union:
        """convert the data back to desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """automatically parametrizes gotten value w
        correct conversion func"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """auto parametizes gotten value w correct
        conversion function"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception as error:
            val = 0
        return val
