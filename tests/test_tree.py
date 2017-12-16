import unittest
from common.tree_factory import BinaryTreeFactory


class BinaryTreeTestCase(unittest.TestCase):
    """ Tests for tree.py """

    def test_perfect_tree(self):
        tree = BinaryTreeFactory.create_perfect_tree()
        print(tree)
        self.assertTrue(True)

    def test_complete_tree(self):
        tree = BinaryTreeFactory.create_complete_tree()
        print(tree)
        self.assertTrue(True)

    def test_full_tree(self):
        tree = BinaryTreeFactory.create_full_tree()
        print(tree)
        self.assertTrue(True)

