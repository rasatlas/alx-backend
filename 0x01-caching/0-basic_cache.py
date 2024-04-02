#!/usr/bin/env python3
""" Module defining a basic caching startegy using dictionary. """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class implementing basic caching using dictionary. """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
