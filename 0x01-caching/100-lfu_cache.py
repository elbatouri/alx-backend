#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict

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
        self.cache_data = OrderedDict()
        self.keys_freq = defaultdict(int)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.keys_freq[key] += 1
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key, _ = min(self.keys_freq.items(), key=lambda x: x[1])
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            self.keys_freq[key] = 1
        else:
            self.keys_freq[key] += 1
