#!/usr/bin/env python3
""" Module implementing an LRU caching mechanism. """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Class implementing an LRU caching mechanism. """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # delete last element from the dictionary.
                tmp = self.cache_data.popitem(last=True)
                print('DISCARD: {}'.format(tmp[0]))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move accessed element to the front.
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
