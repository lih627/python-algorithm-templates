# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ret = 0

        def helper(node, nums):
            if node:
                nums = [node.val + item for item in nums] + [node.val]
                return nums.count(sum) + helper(node.left, nums) + helper(node.right, nums)
            return 0

        return helper(root, [])
