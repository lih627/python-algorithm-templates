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
        from collections import deque
        que = deque([root.left, root.right])
        while que:
            left = que.popleft()
            right = que.popleft()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            else:
                if left.val == right.val:
                    que.extend([left.left, right.right, left.right, right.left])
                else:
                    return False
        return True
