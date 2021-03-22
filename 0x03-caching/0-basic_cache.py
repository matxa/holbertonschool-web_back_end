#!/usr/bin/env python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basics of caching"""

    def put(self, key, item):
        """Add chaching to caching system"""
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        """Get cache from caching system"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
