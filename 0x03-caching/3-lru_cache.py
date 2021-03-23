#!/usr/bin/python3
"""Create a class LRUCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """least recently used caching system"""

    USED = {}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add chaching to caching system"""
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})
            self.USED.update({key: 0})
            if self.cache_data.__len__() > super().MAX_ITEMS:
                pop_item = min(self.USED)
                if self.cache_data.get(pop_item) is not None:
                    self.USED.pop(pop_item)
                    self.cache_data.pop(pop_item)
                print("DISCARD: {}".format(pop_item))

    def get(self, key):
        """Get cache from caching system"""
        if key is None or self.cache_data.get(key) is None:
            return None

        if self.USED.get(key) is not None:
            self.USED[key] += 1
        else:
            self.USED[key] = 1

        return self.cache_data.get(key)
