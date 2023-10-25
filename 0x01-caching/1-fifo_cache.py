#!/usr/bin/env python3

"""
FIFOCache Module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """

    def __init__(self):
        """
        Initialize a FIFOCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = self.order[0]
                self.order = self.order[1:]
                self.cache_data.pop(first_item)
                print("DISCARD:", first_item)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)
