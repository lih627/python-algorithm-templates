"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        stack = []
        node = head
        if not node:
            return node
        while stack or node:
            if node.child:
                if node.next:
                    stack.append(node.next)
                child = node.child
                node.child = None
                node.next = child
                child.prev = node
                node = child
                continue
            if not node.next:
                node.next = stack.pop() if stack else None
                if node.next:
                    node.next.prev = node
                node = node.next
            else:
                node = node.next
        return head
