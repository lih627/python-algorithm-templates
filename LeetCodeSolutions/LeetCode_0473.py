class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        length = sum(nums)
        if length % 4 or nums == []:
            return False
        avg = length // 4
        valid = [True] * n
        edges = [0] * 4
        nums.sort(reverse=True)

        def helper(idx):
            if idx == n:
                return True
            for k in range(4):
                if edges[k] + nums[idx] <= avg:
                    edges[k] += nums[idx]
                    ret = helper(idx + 1)
                    if ret:
                        return True
                    edges[k] -= nums[idx]
            return False

        return helper(0)
