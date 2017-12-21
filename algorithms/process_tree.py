def is_balanced_tree_ver1(root):
    """ the depth of children differs by at most 1 """

    def recursive_check(node):

        if not node:
            return 0, True

        left_height, is_left_balanced = recursive_check(node.left)
        right_height, is_right_balanced = recursive_check(node.right)

        is_subtree_balanced = False
        height = max(left_height, right_height) + 1

        if is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1:
            is_subtree_balanced = True

        return height, is_subtree_balanced

    (_, is_balanced) = recursive_check(root)

    return is_balanced
