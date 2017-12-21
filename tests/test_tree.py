import unittest

from algorithms.process_tree import is_balanced_tree_ver1
from common.logger import log
from common.tree_factory import BinaryTreeFactory


class BinaryTreeTestCase(unittest.TestCase):
    """ Tests """
    def test_perfect_tree(self):
        tree = BinaryTreeFactory.create_perfect_tree()
        log.debug(tree)
        self.assertTrue(True)

    def test_complete_tree(self):
        tree = BinaryTreeFactory.create_complete_tree()
        log.debug(tree)
        self.assertTrue(True)

    def test_full_tree(self):
        tree = BinaryTreeFactory.create_full_tree()
        log.debug(tree)
        self.assertTrue(True)

    def test_is_balanced_tree(self):
        perfect_tree = BinaryTreeFactory.create_perfect_tree()
        log.debug(perfect_tree)
        is_perfect_tree_balanced = is_balanced_tree_ver1(perfect_tree.get_root())
        self.assertTrue(is_perfect_tree_balanced)

        complete_tree = BinaryTreeFactory.create_complete_tree()
        log.debug(complete_tree)
        is_complete_tree_balanced = is_balanced_tree_ver1(complete_tree.get_root())
        self.assertTrue(is_complete_tree_balanced)

        balanced_tree = BinaryTreeFactory.create_balanced_tree()
        log.debug(balanced_tree)
        is_balanced_tree_balanced = is_balanced_tree_ver1(balanced_tree.get_root())
        self.assertTrue(is_balanced_tree_balanced)

        unbalanced_tree = BinaryTreeFactory.create_unbalanced_tree()
        log.debug(unbalanced_tree)
        is_unbalanced_tree_balanced = is_balanced_tree_ver1(unbalanced_tree.get_root())
        self.assertFalse(is_unbalanced_tree_balanced)

    def setUp(self):
        self.trees = []
        self.trees.append(BinaryTreeFactory.create_perfect_tree())
        self.trees.append(BinaryTreeFactory.create_complete_tree())
        self.trees.append(BinaryTreeFactory.create_full_tree())

    def tearDown(self):
        pass
