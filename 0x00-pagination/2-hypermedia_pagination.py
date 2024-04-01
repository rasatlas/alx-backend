#!/usr/bin/env python3
""" Module defining Server class. """


import csv
import math
from typing import Dict, List, Tuple


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
        """ Function that displays paginated pages. """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        self.dataset()
        idx_range = index_range(page, page_size)
        if idx_range[0] > len(self.__dataset)/page_size:
            return []
        else:
            return self.__dataset[idx_range[0]: idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Method: get_hyper with arguments
        Arguments: page and page_size
        """
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        page_info = {
            "page": page,
            "page_size": page_size if page < total_pages else 0,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
            }
        return page_info


def index_range(page: int, page_size: int) -> Tuple:
    """ A function that takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_page = (page * page_size) - page_size
    end_page = start_page + page_size
    return (start_page, end_page)
