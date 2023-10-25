#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initialize an MRUCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                self.cache_data.pop(mru_key)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.order.insert(0, key)

    def get(self, key):
        """
        Get an item from the cache by key and update the order
        """
        if key is not None:
            item = self.cache_data.get(key)
            if item:
                self.order.remove(key)
                self.order.insert(0, key)
            return item
