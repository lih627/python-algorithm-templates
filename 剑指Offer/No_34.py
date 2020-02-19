# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node, tmp, cur_sum):
            cur_sum += node.val
            if not node.left and not node.right:
                if cur_sum == sum:
                    res.append(tmp[:] + [node.val])
                return
            if node.left:
                dfs(node.left, tmp + [node.val], cur_sum)
            if node.right:
                dfs(node.right, tmp + [node.val], cur_sum)

        dfs(root, [], 0)
        return res
