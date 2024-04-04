#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A simple caching system that does not have a limit.
    """

    def put(self, key, item):
        """
        Assigns the item value to the key key in the cache_data dictionary.

        If key or item is None, this method does not do anything.

        :param key: The key to associate with the item.
        :param item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data linked to key.

        If key is None or if the key doesn't exist in cache_data, returns None.

        :param key: The key to retrieve the value for.
        :return: The value associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
