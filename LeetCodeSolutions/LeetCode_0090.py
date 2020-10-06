class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        # print(counter)
        keys = list(counter.keys())
        ret = []
        n = len(counter)

        def helper(idx, tmp):
            if idx == n:
                ret.append(tmp[:])
                return
            num_elems = counter[keys[idx]]
            for i in range(num_elems + 1):
                for j in range(i):
                    tmp.append(keys[idx])
                helper(idx + 1, tmp)
                for j in range(i):
                    tmp.pop()

        helper(0, [])
        return ret
