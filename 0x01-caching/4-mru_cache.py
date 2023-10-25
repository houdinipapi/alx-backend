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

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = max(self.cache_data,
                              key=lambda k: self.cache_data[k])
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key and update the usage
        """
        if key is not None:
            item = self.cache_data.get(key)
            if item:
                del self.cache_data[key]
                self.cache_data[key] = item
            return item
