#!/usr/bin/env python3
""" Module with a simple helper function. """


def index_range(page, page_size):
    """ A function that takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_page = (page * page_size) - page_size
    end_page = start_page + page_size
    return (start_page, end_page)
