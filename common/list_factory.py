from typing import List


class ListFactory:
    @staticmethod
    def create_list():
        arr = list([1, 2, 3, 4])
        arr.extend([5, 6, 7, 8])
        return arr