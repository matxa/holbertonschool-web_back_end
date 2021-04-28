#!/usr/bin/env python3
""" Redis Basics """
import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Init Cache method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Cache
        """
        UUID = str(uuid.uuid4())
        self._redis.set(UUID, data)
        return UUID

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Get key's right format
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if callable(fn):
            value = fn(value)
        return value
