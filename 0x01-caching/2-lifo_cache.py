#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """
        Initialize a LIFOCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.order.pop()
                self.cache_data.pop(last_item)
                print("DISCARD:", last_item)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)
