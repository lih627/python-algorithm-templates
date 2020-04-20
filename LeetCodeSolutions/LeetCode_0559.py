"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def helper(node):
            if not node:
                return 0
            if not node.children:
                return 1
            return max([helper(child) for child in node.children]) + 1

        return helper(root)
