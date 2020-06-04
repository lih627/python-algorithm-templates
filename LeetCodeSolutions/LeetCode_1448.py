# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        from collections import deque
        que = deque()
        que.append([root, float('-inf')])
        while que:
            node, val = que.popleft()
            if node.val >= val:
                cnt += 1
            cur_val = max(val, node.val)
            if node.left:
                que.append([node.left, cur_val])
            if node.right:
                que.append([node.right, cur_val])
        return cnt
