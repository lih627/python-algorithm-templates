# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        que = deque()
        que.append((1, root))
        max_cnt = 0
        while que:
            cur_cnt, node = que.popleft()
            max_cnt = max(max_cnt, cur_cnt)
            if node.left:
                que.append(((cur_cnt + 1), node.left))
            if node.right:
                que.append(((cur_cnt + 1), node.right))
        return max_cnt
