"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        pre, nxt = head, head.next
        while nxt != head:
            if pre.val > nxt.val:
                if insertVal <= nxt.val or insertVal >= pre.val:
                    break
            if pre.val <= insertVal <= nxt.val:
                break
            else:
                pre = pre.next
                nxt = nxt.next
        node = Node(insertVal)
        node.next = nxt
        pre.next = node
        return head
