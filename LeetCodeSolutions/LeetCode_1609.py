# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        que = deque()
        que.append(root)
        level = 0
        while que:
            n_nodes = len(que)
            tmp = []
            odd = False
            if level & 1:
                odd = True
            for _ in range(n_nodes):
                node = que.popleft()
                if odd:
                    if node.val & 1:
                        return False
                else:
                    if node.val & 1 == 0:
                        return False
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # print(tmp, level, odd)
            if odd:
                i = 0
                while i < len(tmp) - 1:
                    if tmp[i] <= tmp[i + 1]:
                        return False
                    i += 1
            else:
                i = 0
                while i < len(tmp) - 1:
                    if tmp[i] >= tmp[i + 1]:
                        return False
                    i += 1
            level += 1
        return True
