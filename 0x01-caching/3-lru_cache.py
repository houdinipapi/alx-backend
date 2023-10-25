#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        """
        Initialize an LRUCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                self.cache_data.pop(lru_key)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item from the cache by key and update the order
        """
        if key is not None:
            item = self.cache_data.get(key)
            if item:
                self.order.remove(key)
                self.order.append(key)
            return item
