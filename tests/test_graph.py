import unittest

from algorithms.process_tree import is_balanced_tree_ver1
from common.logger import log
from common.graph_factory import GraphFactory


class UndirectedGraphTestCase(unittest.TestCase):
    """ Tests """
    def test_simple_graph(self):
        graph = GraphFactory.create_graph()
        log.debug(graph)
        self.assertTrue(True)

    def setUp(self):
        pass

    def tearDown(self):
        pass
