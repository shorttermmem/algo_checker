from common.linkedlist_factory import Node, LinkedList

def traverse2pointers(head: Node) -> Node:
    """ iterate through linkedlist with two pointers """

    if not head: return

    slow, fast, llist = head, head, LinkedList(head)

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow, fast
