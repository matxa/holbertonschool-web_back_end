#!/usr/bin/env python3
""" Redis Basics """
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count how many times a method is called
    """
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ Wrapper function for decorator
        """
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ History of input and output
    """
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ Wrapper function for decorator
        """
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        self._redis.rpush("{}:outputs".format(
            method.__qualname__), method(self, *args))
        return method(self, *args)
    return wrapper


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Init Cache method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_int(self, k: int) -> int:
        """ convert bytes to int
        """
        return self.get(k, int)
