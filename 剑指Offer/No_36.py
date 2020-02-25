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
        if not root:
            return root
        tmp = []

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            tmp.append(node)
            inorder(node.right)

        inorder(root)
        n = len(tmp)
        for idx, node in enumerate(tmp):
            node.left = tmp[idx - 1]
            node.right = tmp[(idx + 1) % n]
        return tmp[0]

    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        before = None
        head = stack[-1]
        while stack:
            cur = stack.pop()
            tmp = cur.right
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            if stack:
                after = stack[-1]
            else:
                after = head
            cur.left = before
            cur.right = after
            before = cur
        head.left = before
        return head
