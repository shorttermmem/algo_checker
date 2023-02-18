from common.logger import log


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


def walk_inorder(node):
    if node is None:
        return
    walk_inorder(node.left)
    log.info(node)
    walk_inorder(node.right)


def walk_preorder(node):
    if node is None:
        return
    log.info(node)
    walk_preorder(node.left)
    walk_preorder(node.right)


def walk_postorder(node):
    if node is None:
        return
    walk_postorder(node.left)
    walk_postorder(node.right)
    log.info(node)


