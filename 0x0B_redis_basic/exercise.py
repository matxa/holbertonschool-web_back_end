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
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, k: str) -> str:
        """ convert bytes to str
        """
        return self.get(k, str)

    def get_str(self, k: int) -> int:
        """ convert bytes to int
        """
        return self.get(k, int)
