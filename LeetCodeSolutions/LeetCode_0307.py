class FenwickTree:
    def __init__(self, nums):
        '''
        Fenwick Tree or Binary Indexed Tree(BIT)
        :param nums:
        '''
        self.BIT_arr = [0] * (len(nums) + 1)
        # O(nlogn)
        # for idx, _ in enumerate(nums):
        #     self.update(idx, _)
        # O(n)
        for i in range(len(nums)):
            self.BIT_arr[i + 1] = nums[i]
        for i in range(1, len(self.BIT_arr)):
            j = i + self.lowbit(i)
            if j < len(self.BIT_arr):
                self.BIT_arr[j] += self.BIT_arr[i]

    def lowbit(self, idx):
        return idx & -idx

    def update(self, idx, delta):
        idx += 1
        while idx < len(self.BIT_arr):
            self.BIT_arr[idx] += delta
            idx += self.lowbit(idx)

    def prefixSum(self, idx):
        idx += 1
        ans = 0
        while idx > 0:
            ans += self.BIT_arr[idx]
            idx -= self.lowbit(idx)
        return ans

    def rangeSum(self, idx1, idx2):
        return self.prefixSum(idx2) - self.prefixSum(idx1 - 1)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.Fenwick = FenwickTree(nums)

    def update(self, i: int, val: int) -> None:
        self.Fenwick.update(i, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.Fenwick.rangeSum(i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
