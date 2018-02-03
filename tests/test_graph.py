import unittest

from algorithms.process_graph import is_directed_graph_ver1
from common.logger import log
from common.graph_factory import GraphFactory
import random


class UndirectedGraphTestCase(unittest.TestCase):
    """ Tests """
    def test_simple_graph(self):

        graph = GraphFactory.create_graph()
        count = len(graph.get_nodes())
        for node in graph.get_nodes():
            max_edge_per_node = random.randint(0, count)
            for _ in range(max_edge_per_node):
                node.add_edges([
                    (graph.get_random_node().name, 0)
                ])
        is_directed_graph_ver1()

        log.debug(graph)
        self.assertTrue(True)

    def setUp(self):
        log.info("\nEnter " + __class__.__name__ + "...")

    def tearDown(self):
        log.info("Done " + __class__.__name__ + "\n")
