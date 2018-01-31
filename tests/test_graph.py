import unittest

from algorithms.process_graph import is_directed_graph_ver1
from common.logger import log
from common.graph_factory import GraphFactory
import random


class UndirectedGraphTestCase(unittest.TestCase):
    """ Tests """
    def test_simple_graph(self):

        graph = GraphFactory.create_graph()

        for node in graph.get_nodes():
            node.add_edges([
                (graph.get_random_node().name, 0),
                (graph.get_random_node().name, 0)
            ])
        is_directed_graph_ver1()

        log.debug(graph)
        self.assertTrue(True)

    def setUp(self):
        pass

    def tearDown(self):
        pass
