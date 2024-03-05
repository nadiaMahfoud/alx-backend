#!/usr/bin/python3
"""Create a class LFUCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call
the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU
algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by
a new line def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.
cache_data, return None. """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """Retrieves an item by key."""
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
