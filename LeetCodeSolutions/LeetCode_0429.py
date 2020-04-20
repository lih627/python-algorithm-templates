"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        from collections import deque
        que = deque()
        que.append(root)
        while que:
            n = len(que)
            tmp = []
            for _ in range(n):
                node = que.popleft()
                tmp.append(node.val)
                for child in node.children:
                    que.append(child)
            res.append(tmp)
        return res
