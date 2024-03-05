#!/usr/bin/python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.
If key or item is None, this method should not do
anything.
def get(self, key):
Must return the value in self.cache_data linked
to key.
If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary."""

    def put(self, key, item):
        """Adds an item in the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key)
