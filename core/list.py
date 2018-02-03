import random
from enum import Enum


class ArrayList:

    class Item:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return '{0}'.format(self.value)

    def __init__(self, *args, max_size=None):
        args_array = list(*args)
        extend_size = None
        self.max_size = max_size

        if self.max_size is not None:
            extend_size = self.max_size - len(args_array)

        # check args size < max_size
        if extend_size is not None and extend_size < 0:
            raise TypeError('Input array exceeds max size')

        # copy of args size
        self._data = [ArrayList.Item(arg) for arg in args_array]

        if extend_size is not None:
            self._data.extend([None] * extend_size)

    def extend(self, *args):
        args_array = list(*args)
        new_size = len(args_array) + len(self._data)

        if self.max_size is not None:
            if new_size >= self.max_size:
                raise KeyError('Extend beyond max size')
        self._data.extend(args_array)

    def __setitem__(self, key, value):
        ArrayList.index_exists(key, self._data)
        self._data[key] = value

    def __getitem__(self, key):
        ArrayList.index_exists(key, self._data)
        return self._data[key]

    def __delitem__(self, idx):
        for i in range(idx, self.max_size - 1):
            self._data[i] = self._data[i - 1]
        self.max_size = self.max_size - 1

    def __iter__(self):
        for item in self._data:
            yield item

    def __len__(self):
        return len(self._data)

    def __str__(self):
        if self.max_size is None:
            size = len(self._data)
        else:
            size = self.max_size
        return 'Array[' + str(size) + ']: ' + ', '.join(str(item) for item in self._data)

    @staticmethod
    def index_exists(key, data):
        if not 0 <= key < len(data):
            raise KeyError('Invalid key')


class LinkedList:
    pass
