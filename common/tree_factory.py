from common.logger import log
from core.tree import Node, Tree
from core.tree import TreeFromArray


class BinaryTreeFactory:
    @staticmethod
    def create_perfect_tree():
        """Tree: {None: 4}{4: 2}{4: 6}{2: 1}{2: 3}{6: 5}{6: 7}"""
        tree = Tree()
        tree.insert(Node(4, parent_name=None))
        tree.insert(Node(2, parent_name=4))
        tree.insert(Node(6, parent_name=4))
        tree.insert(Node(1, parent_name=2))
        tree.insert(Node(3, parent_name=2))
        tree.insert(Node(5, parent_name=6))
        tree.insert(Node(7, parent_name=6))
        return tree

    @staticmethod
    def create_complete_tree():
        """Tree: {None: 4}{4: 2}{4: 6}{2: 1}{2: 3}{6: 5}"""
        tree = Tree()
        tree.insert(Node(4, parent_name=None))
        tree.insert(Node(2, parent_name=4))
        tree.insert(Node(6, parent_name=4))
        tree.insert(Node(1, parent_name=2))
        tree.insert(Node(3, parent_name=2))
        tree.insert(Node(5, parent_name=6))
        return tree

    @staticmethod
    def create_full_tree():
        """Tree: {None: 1}{1: 2}{1: 3}{3: 6}{3: 7}"""
        tree = Tree()
        tree.insert(Node(4, parent_name=None))
        tree.insert(Node(2, parent_name=4))
        tree.insert(Node(6, parent_name=4))
        tree.insert(Node(5, parent_name=6))
        tree.insert(Node(7, parent_name=6))
        return tree

    @staticmethod
    def create_balanced_tree():
        """Tree: {None: 1}{1: 2}{1: 3}{2:4}{3: 6}{3: 7}"""
        tree = Tree()
        tree.insert(Node(4, parent_name=None))
        tree.insert(Node(2, parent_name=4))
        tree.insert(Node(6, parent_name=4))
        tree.insert(Node(3, parent_name=2))
        tree.insert(Node(5, parent_name=6))
        tree.insert(Node(7, parent_name=6))
        return tree

    @staticmethod
    def create_unbalanced_tree():
        """Tree: {None: 1}{1: 2}{1: 3}{3: 6}{3: 7}{6: 8}"""
        tree = Tree()
        log.debug(tree.get_root())

        tree.insert(Node(4, parent_name=None))
        tree.insert(Node(2, parent_name=4))
        tree.insert(Node(6, parent_name=4))
        tree.insert(Node(1, parent_name=2))
        tree.insert(Node(5, parent_name=6))
        tree.insert(Node(7, parent_name=6))
        tree.insert(Node(8, parent_name=7))
        tree.insert(Node(9, parent_name=8))
        return tree


class TreeFromArrayFactory:
    @staticmethod
    def create_binary_tree():
        arr = [0, 1, 2, 3, 4, 5]
        return TreeFromArray(arr)

    @staticmethod
    def create_perfect_tree(height):
        """ node count n is 2 ^ h """
        n = pow(2, height)
        arr = range(0, n - 1)
        return TreeFromArray(arr)




