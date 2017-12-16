import unittest

from core.tree import Node, Tree, TreeFactory


class BinaryTreeTestCase(unittest.TestCase):
    """ Tests for tree.py """

    def test_is_binarytree(self):
        """ Is every node of the tree
        has at most two children"""

        btree = TreeFactory.create_binary_tree()
        #print(btree)
        self.assertTrue(btree.is_binary_tree(),
                        msg='Binary tree should has at most two children per node')

    def test_perfect_tree(self):
        ptree = TreeFactory.create_perfect_tree(4)
        #print(ptree)
        self.assertTrue(ptree.is_binary_tree(),
                        msg='failed')

    def test_custom_tree(self):
        btree = Tree()
        btree.insert(Node(1))
        print(btree)
        btree.insert(Node(2, parent_name=1))
        btree.insert(Node(3, parent_name=1))
        print(btree)
        btree.insert(Node(4, parent_name=2))
        print(btree)
        btree.insert(Node(5, parent_name=2))
        btree.insert(Node(6, parent_name=3))
        btree.insert(Node(7, parent_name=3))

        print(btree)
        self.assertTrue(btree.is_binary_tree(), msg='failed')

        other_tree = Tree()
        other_tree.insert(Node(1))
        other_tree.insert(Node(2, parent_name=1))
        other_tree.insert(Node(3, parent_name=1))
        other_tree.insert(Node(4, parent_name=2))
        other_tree.insert(Node(5, parent_name=2))
        other_tree.insert(Node(6, parent_name=3))
        other_tree.insert(Node(7, parent_name=3))

        self.assertTrue(btree == other_tree, msg='The trees are not equal.')

