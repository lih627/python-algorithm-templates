"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [[root, False]]
        res = []
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append([node, True])
                for _node in node.children[::-1]:
                    stack.append([_node, False])
            else:
                res.append(node.val)
        return res
