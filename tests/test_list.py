import unittest

from algorithms.process_list import *
from common.logger import log
from common.list_factory import ArrayListFactory
from core.list import ArrayList


class MergeSortTestCase(unittest.TestCase):
    def test_simple_array(self):
        arr_b = ArrayListFactory.create_array_list()
        arr_a = ArrayList(['A', 'A', 'A', 'A'], max_size=len(arr_b) + 4)
        log.debug(arr_a)
        log.debug(arr_b)
        self.assertTrue(True)

    def setUp(self):
        log.info("Enter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")
