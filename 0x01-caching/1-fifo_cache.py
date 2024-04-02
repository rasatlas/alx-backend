#!/usr/bin/env python3
""" Module implementing a FIFO caching mechanism. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class implementing FIFO caching mechanism. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                my_tuple = self.cache_data.popitem()
                print('DISCARD: {}'.format(my_tuple[0]))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
