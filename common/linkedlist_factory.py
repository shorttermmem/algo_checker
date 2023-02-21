class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self, node = None):
        self.head = node # wrap any node as linkedlist

    def __repr__(self):
        node = self.head
        nodes = []
        while not node:
            nodes.append(node.val)
            node = node.next
        return "->".join(nodes)

class LinkedListFactory:
    @staticmethod
    def create_linked_list(length = 10):
        head = curr = Node()

        for i in range(0, length):
            curr.next = Node(i)
            curr = curr.next
        return LinkedList(head.next)