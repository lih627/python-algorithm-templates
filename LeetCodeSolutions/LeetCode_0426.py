"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # left : pre right: nex
        dummy = Node(None)
        p = dummy
        if not root:
            return root
        stack = [[root, False]]
        while stack:
            node, visited = stack.pop()
            if not visited:
                if node.right:
                    stack.append([node.right, False])
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
            else:
                node.left = p
                node.right = None
                p.right = node
                p = p.right
        head = dummy.right
        head.left = p
        p.right = head
        return head
