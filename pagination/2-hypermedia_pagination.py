#!/usr/bin/env python3
"""Takes two inteeger arguments page and page_size"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """Returns the requested page"""
        assert(type(page) == int and page > 0)
        assert(type(page_size) == int and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing key-value pairs"""
        dataset = self.dataset()
        total_records = len(dataset)
        total_pages = math.ceil(total_records / page_size)

        if page == total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        current_page = self.get_page(page, page_size)

        output = {
            'page_size': len(current_page),
            'page': page,
            'data': current_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return output
