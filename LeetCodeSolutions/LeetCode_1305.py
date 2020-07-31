# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        from collections import deque
        dq1 = deque()
        dq2 = deque()
        if root1:
            dq1.append([root1, False])
        if root2:
            dq2.append([root2, False])
        nums1, nums2 = [], []
        for dq, nums in zip([dq1, dq2], [nums1, nums2]):

            while dq:
                node, visited = dq.popleft()
                if not visited:
                    if node.right:
                        dq.appendleft([node.right, False])
                    dq.appendleft([node, True])
                    if node.left:
                        dq.appendleft([node.left, False])
                else:
                    nums.append(node.val)
        print(nums1, nums2)
        ret = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums[j])
                j += 1
        ret.extend(nums1[i:] + nums2[j:])
        print(ret)

        return ret
