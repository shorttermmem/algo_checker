from queue import Queue


class Node:
    """ Tree node """

    def __init__(self, node_name, node_data=None, parent_name=None, max_children=2):
        self.name = node_name
        self.data = node_data,
        self.children = [None, None]
        self.left = self.children[0]
        self.right = self.children[1]
        """private members"""
        self._parent_name = parent_name
        self._count = 0
        self._max_count = max_children

    def __eq__(self, other):
        if not self or not other:
            return False
        return self.name == other.name

    def __str__(self):
        return '{{ {0}:{1} }}'.format(self._parent_name, self.name)

    def add_child(self, child):
        if self._count < 2:
            self.children[self._count] = child
        else:
            if len(self.children) == self._max_count:
                raise Exception('Exceeds max number of children.')
            else:
                self.children.append(child)
        self._count += 1
        return True

    def get_children(self):
        for child in self.children:
            if child:
                yield child

    def get_parent_name(self):
        return self._parent_name


def walk_bfs(root, lambda_fn=None, lambda_arg=None):
    q = Queue()
    q.put(root)
    while not q.empty():
        visit_node = q.get()
        if lambda_fn:
            if lambda_fn(visit_node, lambda_arg):
                return visit_node
        for unvisited_node in visit_node.get_children():
            q.put(unvisited_node)
    return


def walk_dfs(root, lambda_fn=None, lambda_arg=None):
    if not root:
        return
    if lambda_fn:
        if lambda_fn(root, lambda_arg):
            return root
    for child in root.get_children():
        walk_dfs(child, lambda_fn, lambda_arg)


def same_tree(root1, root2, lambda_fn=None, lambda_arg=None):
    # Check root
    if root1 != root2:
        return False

    for child1, child2 in zip(root1.get_children(), root2.get_children()):
        if not lambda_fn(child1, child2, lambda_arg):
            return False
        else:
            same_tree(child1, child2, lambda_fn, lambda_arg)
    return True


class Tree:
    def __init__(self):
        self._root = None

    def __str__(self):
        tree_list = list("Tree: ")
        walk_bfs(
            self._root,
            lambda node, out_list: out_list.extend(list(str(node))),
            tree_list)
        return "".join(tree_list)

    def __repr__(self):
        self.__str__()

    def __eq__(self, other_tree):
        if not isinstance(other_tree, Tree):
            raise Exception('The other tree must be of a tree type')
        return same_tree(self._root, other_tree.get_root(), lambda x, y, _: x.name == y.name)

    def get_root(self):
        return self._root

    def insert(self, node):
        if not node:
            return True
        elif not self._root:
            self._root = node
        else:
            target = walk_bfs(self._root, lambda x, y: x.name == y, node.get_parent_name())
            if not target:
                raise Exception('Parents not found for {0}.'.format(node))
            return target.add_child(node)

    def delete(self, node):
        pass

    def is_binary_tree(self):
        return self._root is not None


class TreeFromArray(Tree):
    def __init__(self, arr):
        Tree.__init__(self)
        if arr is None:
            self.count = 0
            self.height = 0
        else:
            self.count = len(arr)
            self._root = TreeFromArray.add_nodes(0, self.count - 1, arr)

    @staticmethod
    def add_nodes(left, right, arr):

        if left > right:
            return None

        middle = (left + right + 1) // 2
        new_node = Node(middle, arr[middle])

        # print(' ' + str(arr[middle]) + ' ')

        new_node.left = TreeFromArray.add_nodes(left, middle - 1, arr)
        new_node.right = TreeFromArray.add_nodes(middle + 1, right, arr)

        return new_node

    @staticmethod
    def print_nodes(node):
        if node is None:
            return ''

        str_tree = ''

        # left branch
        ldata = TreeFromArray.print_nodes(node.left)

        if ldata:
            str_tree += ('{' + ldata + ' -> ')

        # visit
        str_tree += str(node.name)

        # right branch
        rdata = TreeFromArray.print_nodes(node.right)

        if rdata:
            str_tree += (' <- ' + rdata + '}')

        return str_tree

    def __str__(self):
        return TreeFromArray.print_nodes(self._root)

    def __repr__(self):
        return TreeFromArray.print_nodes(self._root)

    def is_binary_tree(self):
        return self._root is not None


class TreeFactory:
    @staticmethod
    def create_binary_tree():
        arr = [0, 1, 2, 3, 4, 5]
        return TreeFromArray(arr)

    @staticmethod
    def create_perfect_tree(height):
        """ node count n is 2 ^ h """
        n = pow(2, height)
        arr = range(0, n-1)
        return TreeFromArray(arr)


