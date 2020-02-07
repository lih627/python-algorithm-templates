class FenwickTree:
    def __init__(self, nums):
        '''
        Fenwick Tree or Binary Indexed Tree(BIT)
        :param nums:
        '''
        self.nums = nums
        self.BIT_arr = [0] * (len(nums) + 1)
        # O(nlogn)
        # for idx, _ in enumerate(nums):
        #     self._add(idx, _)
        # O(n)
        for i in range(len(nums)):
            self.BIT_arr[i + 1] = nums[i]
        for i in range(1, len(self.BIT_arr)):
            j = i + self.lowbit(i)
            if j < len(self.BIT_arr):
                self.BIT_arr[j] += self.BIT_arr[i]

    def lowbit(self, idx):
        return idx & -idx

    def _add(self, idx, delta):
        '''
        nums[idx] += delta
        '''
        idx += 1
        while idx < len(self.BIT_arr):
            self.BIT_arr[idx] += delta
            idx += self.lowbit(idx)

    def update(self, idx, val):
        self._add(idx, val - self.nums[idx])
        self.nums[idx] = val

    def prefixSum(self, idx):
        idx += 1
        ans = 0
        while idx > 0:
            ans += self.BIT_arr[idx]
            idx -= self.lowbit(idx)
        return ans

    def rangeSum(self, idx1, idx2):
        return self.prefixSum(idx2) - self.prefixSum(idx1 - 1)


if __name__ == '__main__':
    nums = [1, 3, 5, 7, 8]
    BIT = FenwickTree(nums)
    print(BIT.rangeSum(0, 2))
    print(BIT.BIT_arr)
    BIT.update(1, 2)
    print(BIT.rangeSum(0, 2))
    print(BIT.BIT_arr)
