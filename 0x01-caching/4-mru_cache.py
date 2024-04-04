#!/usr/bin/env python3
"""MRU caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that uses the MRU algorithm to manage the cache.
    """

    def __init__(self):
        """
        Initializes the MRUCache object.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns the item value to the key key in the cache_data dictionary.

        If key or item is None, this method does not do anything.

        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS: you must discard the most recently used item
        (MRU algorithm) and print DISCARD: with the key discarded and
        following by a new line.

        :param key: The key to associate with the item.
        :param item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key[0]}")

    def get(self, key):
        """
        Returns the value in cache_data linked to key.

        If key is None or if the key doesn't exist in cache_data,
        return None.

        :param key: The key to retrieve the value for.
        :return: The value with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
