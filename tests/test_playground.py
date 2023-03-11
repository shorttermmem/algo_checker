import unittest

from common.logger import log
from common.list_factory import ListFactory

class Playground(unittest.TestCase):
    def test_main(self):
        l = ListFactory.create_list()
        for pair in zip(l[:-1], l[1:]):
            print(pair)

    def setUp(self):
        log.info("Enter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")
