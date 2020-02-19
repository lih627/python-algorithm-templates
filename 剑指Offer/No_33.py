class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        def helper(nums, minv, maxv):
            if not nums:
                return True
            root = nums[-1]
            if root < minv or root > maxv:
                return False
            idx = 0
            while idx < len(nums) - 1:
                if nums[idx] > root:
                    break
                idx += 1
            return helper(nums[:idx], minv, root) and helper(nums[idx: -1], root, maxv)

        res = helper(postorder, minv=float('-inf'), maxv=float('inf'))
        return res
