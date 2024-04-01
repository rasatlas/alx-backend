#!/usr/bin/env python3
""" Module defining Server class. """


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0

        self.dataset()
        idx_range = index_range(page, page_size)
        if idx_range[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[idx_range[0]: idx_range[1]]


def index_range(page, page_size):
    """ A function that takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_page = (page * page_size) - page_size
    end_page = start_page + page_size
    return (start_page, end_page)
