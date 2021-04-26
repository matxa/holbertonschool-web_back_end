#!/usr/bin/env python3
""" Redis Basics """
import redis
import uuid


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Init Cache method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str or bytes or int or float) -> str:
        """ Store data in Cache
        """
        UUID = str(uuid.uuid4())
        self._redis.set(UUID, data)
        return UUID
