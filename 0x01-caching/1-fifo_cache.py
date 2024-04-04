#!/usr/bin/env python3
"""FIFO caching module.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that uses the FIFO algorithm to manage the cache.
    """

    def __init__(self):
        """
        Initializes the FIFOCache object.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns the item value to the key key in the cache_data dictionary.

        If key or item is None, this method does not do anything.

        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS: you must discard the first item put in cache
        (FIFO algorithm) and print DISCARD: with the key discarded and
        following by a new line.

        :param key: The key to associate with the item.
        :param item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Returns the value in cache_data linked to key.

        If key is None or if the key doesn't exist in cache_data,
        return None.

        :param key: The key to retrieve the value for.
        :return: The value ith the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
