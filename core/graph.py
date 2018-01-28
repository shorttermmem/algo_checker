import random
from enum import Enum


class Graph:
    """ Implemented as Adjacency-list """
    _ref_link = "https://xlinux.nist.gov/dads/HTML/adjacencyListRep.html"
    SELF_REFERENCING_EDGE_WEIGHT = 0

    class Node:
        """ Graph node """
        def __init__(self, node_name, node_weight=0):
            self.name = node_name
            self.weight = node_weight
            """ private """
            edge = (node_name, node_weight)
            self._edges = {edge}

        def add_edges(self, *edges):
            """ edges are array of tuples(node_name, weight=0) """
            convert_to_set = set(edges)
            self._edges.union(convert_to_set)

        def get_edges(self):
            return list(self._edges)

        def __str__(self):
            return "<" + self.name + ":" + str(self.weight) + ">"

    class Type(Enum):
        """ Graph types """
        DEFAULT = 0
        DIRECTED = 1

    def __init__(self, graph_type=Type.DEFAULT, node_count=0):
        """ private """
        self._graph_type = graph_type
        self._nodes = set([
            Graph.Node(str(node_name), Graph.SELF_REFERENCING_EDGE_WEIGHT) for node_name in range(node_count)
        ])

    @property
    def type(self):
        return self._graph_type

    def get_node(self, node_name):
        """ extract node with the same name """
        return next((node for node in self._nodes if node.name == node_name), None)

    def add_node(self, node_name, node_weight=0):
        self._nodes.add(Graph.Node(node_name, node_weight))

    def get_neighbors(self, node_name):
        """ extract node name from all edges of a node """
        return map(lambda edge: edge[0], self.get_node(node_name).get_edges())

    def __str__(self):
        return " ".join(str(node) for node in self._nodes)


class DeprecatedGraph:
    def __init__(self):
        self.m_data = [[]]

    def create_matrix(self, rows, cols):
        # Create 2D matrix
        self.m_data = [[random.randint(1, 15) for _ in range(cols)] for _ in range(rows)]

    def create_array(self, size):
        self.m_data = [random.randint(1, 5) for _ in range(size)]

    def __repr__(self):

        # Convert data into 2d literal string
        line = [[str(_) for _ in row] for row in self.m_data]

        # Get column-wise max integer digit counts
        max_col_lens = [max(map(len, col)) for col in zip(*line)]

        # Format string by setting unit space per number
        # "{" [field_name] ["!" conversion] [":" format_spec] "}"
        fmt = '\t'.join('{{:{}}}'.format(_) for _ in max_col_lens)

        # Re-format table
        table = [fmt.format(*row) for row in line]

        return '\n'.join(table)


