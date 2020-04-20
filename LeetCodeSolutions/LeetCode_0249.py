class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def helper(strs):
            MOD_N = 26
            ans = ''
            for idx, s in enumerate(strs):
                if idx == 0:
                    ans += '0'
                    continue
                tmp = (ord(s) - ord(strs[idx - 1])) % MOD_N
                ans += str(tmp)
            return ans

        d = {}
        for s in strings:
            k = helper(s)
            if k not in d:
                d[k] = [s]
            else:
                d[k].append(s)

        return [_ for _ in d.values()]
