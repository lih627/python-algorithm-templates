# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        l = root.left
        r = root.right
        if not l or not r:
            return not l and not r
        if l.val != r.val:
            return False
        from collections import deque
        q = deque()
        q.append((l, r))
        res = True
        while res and q:
            l, r = q.popleft()
            if not l or not r:
                if l or r:
                    res = False
                    break
                else:
                    continue
            else:
                if l.val != r.val:
                    res = False
                else:
                    q.append((l.left, r.right))
                    q.append((l.right, r.left))
        return res
