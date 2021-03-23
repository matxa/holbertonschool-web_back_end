#!/usr/bin/python3
"""Create a class FIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add chaching to caching system"""
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})
            if self.cache_data.__len__() > super().MAX_ITEMS:
                cache_list = list(self.cache_data)
                first_key = cache_list[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Get cache from caching system"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
