import unittest
import math

from algorithms.process_list import *
from algorithms.process_linkedlist import *
from common.logger import log
from common.list_factory import ListFactory
from common.linkedlist_factory import LinkedListFactory, Node, LinkedList

class MergeSortTestCase(unittest.TestCase):
    def test_simple_array(self):
        arr_b = ListFactory.create_list()
        log.debug(arr_b)
        self.assertTrue(True)

    def test_findKthLargest(self):
        arr = ListFactory.create_list()
        res = findKthLargest(arr, 3)
        self.assertTrue(res == 6)

    def setUp(self):
        log.info("Enter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")

class LinkedListTestCase(unittest.TestCase):
    def test_linked_list(self):
        llist = LinkedListFactory.create_linked_list()

        slow, fast = traverse2pointers(llist.head)
        self.assertTrue(slow.val == 5)
        self.assertTrue(fast is None)

    def setUp(self):
        log.info("Enter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")

class CombinatoricsTestCase(unittest.TestCase):
    def test_permutations(self):
        nums = ListFactory.create_list()
        n = len(nums)
        k = 2
        res = findPermutations(nums, k)
        self.assertTrue(
            len(res) ==
            math.factorial(n) / math.factorial(n-k))
        log.debug(res)

    def setUp(self):
        log.info("Enter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")