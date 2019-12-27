from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        n = self
        s = ''
        while n:
            s += str(n.val)
            if n.next:
                s += ' -> '
            n = n.next
        return s

    __str__ = __repr__


def linked_list(l: List[any]):
    if not l:
        return None

    head = ListNode(l[0])
    cur = head
    for elem in l[1:]:
        cur.next = ListNode(elem)
        cur = cur.next
    return head
