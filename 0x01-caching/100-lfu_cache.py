#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import defaultdict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an LFU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = min(self.frequency.items(),
                                 key=lambda x: x[1],
                                 default=(None, BaseCaching.MAX_ITEMS + 1))
                if lru_key is None:
                    break
                self.cache_data.pop(lru_key)
                self.frequency.pop(lru_key)
                print("DISCARD:", lru_key)
            self.frequency[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
        return self.cache_data.get(key, None)
