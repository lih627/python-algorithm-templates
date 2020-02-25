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


class FenwickTree_2:
    '''
    FenwickTree 可用于数组逆序对统计
    '''
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def __lowbit(self, index):
        return index & (-index)

    def update(self, index, delta):
        # 单点更新
        while index < self.size + 1:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index):
        # 区间查询 or 前缀和
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res


def count_reversePairs(nums: list) -> int:
    """
    LeetCode 0315  liweiwei 的答案
    1. 数据离散化, 对数字大小通过rank 排名
    2. 逆序遍历数组, 更新树状数组
    3. 查询树状数组当前更新索引的前缀和,
       为当前这个数相关的逆序对个数
    """
    # refer to liweiwei's solution
    size = len(nums)
    if size < 2:
        return 0
    s = list(set(nums))
    import heapq
    heapq.heapify(s)
    rank_map = {}
    rank = 1
    rank_map_size = len(s)
    for _ in range(rank_map_size):
        num = heapq.heappop(s)
        rank_map[num] = rank
        rank += 1

    res = 0
    fenwicktree = FenwickTree_2(rank_map_size)
    # 数组逆序遍历
    for i in range(size - 1, -1, -1):
        rank = rank_map[nums[i]]
        fenwicktree.update(rank, 1)
        res += fenwicktree.query(rank - 1)
    return res

if __name__ == '__main__':
    nums = [1, 3, 5, 7, 8]
    BIT = FenwickTree(nums)
    print(BIT.rangeSum(0, 2))
    print(BIT.BIT_arr)
    BIT.update(1, 2)
    print(BIT.rangeSum(0, 2))
    print(BIT.BIT_arr)
    print(count_reversePairs([1, 3, 2, 4, 5]))
