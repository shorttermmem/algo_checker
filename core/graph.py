import random
from enum import Enum


class Graph:
    """ Implemented as Adjacency-list """
    _ref_link = "https://xlinux.nist.gov/dads/HTML/adjacencyListRep.html"
    SELF_REFERENCING_EDGE_WEIGHT = None

    class Node:
        """ Graph node """
        def __init__(self, node_name, node_data=0):
            self.name = node_name
            self.data = node_data
            """ private """
            # _edges is (node_name, node_data)
            self._edges = set()

        def add_edges(self, *edges):
            """ edges are array of tuples(node_name, weight=0) """
            self._edges.update(set(*edges))

        def get_edges(self):
            return list(self._edges)

        def get_neighbors(self):
            """ extract node name from all edges of a node """
            return map(lambda edge: edge[0], self.get_edges())

        def __str__(self):
            return "\tNode<" + str(self.name) + ":" + str(self.data) + ">:" + "->".join(
                [" edge(" + str(edge[0]) + ", " + str(edge[1]) + ") " for edge in self._edges]
            )

    class Type(Enum):
        """ Graph types """
        DEFAULT = 0
        DIRECTED = 1

    def __init__(self, node_count, graph_type=Type.DEFAULT):
        """ private """
        self._graph_type = graph_type
        self._nodes = set([
            Graph.Node(name, Graph.SELF_REFERENCING_EDGE_WEIGHT) for name in range(node_count)
        ])

    @property
    def type(self):
        return self._graph_type

    def get_node(self, node_name):
        """ extract node with the same name """
        return next(iter(node for node in self._nodes if node.name == node_name), None)

    def get_random_node(self):
        return random.choice(tuple(self._nodes))

    def add_node(self, node_name, node_data=0):
        self._nodes.add(Graph.Node(node_name, node_data))

    def get_nodes(self):
        return list(self._nodes)

    def __str__(self):
        return "Graph\n" + "\n".join(str(node) for node in sorted(self._nodes, key=lambda node: node.name))


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


