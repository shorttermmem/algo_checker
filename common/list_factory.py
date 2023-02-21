from core.list import ArrayList


class ArrayListFactory:
    @staticmethod
    def create_array_list():
        arr = ArrayList([1, 2, 3, 4])
        arr.extend([5, 6, 7, 8])
        return arr