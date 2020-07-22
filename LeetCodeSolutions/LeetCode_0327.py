class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        prefix, ret = 0, 0
        st = SortedList([0])
        for num in nums:
            prefix += num
            ret += st.bisect_right(prefix - lower) - st.bisect_left(prefix - upper)
            st.add(prefix)
        return ret
