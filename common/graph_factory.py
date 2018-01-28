from core.graph import Graph
from core.graph import DeprecatedGraph


class GraphFactory:
    @staticmethod
    def create_graph():
        return Graph(node_count=10)




