class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ret, l, r = 0, 0, 0
        cnt = dict()
        hash_set = set()
        while r < len(s):
            cs = s[r]
            # print(hash_set, cnt, l, r)
            if cs not in cnt:
                cnt[cs] = 1
            else:
                cnt[cs] += 1
            hash_set.add(cs)
            if len(hash_set) > 2:
                while cnt[s[l]] != 1:
                    cnt[s[l]] -= 1
                    l += 1
                cnt[s[l]] -= 1
                hash_set.remove(s[l])
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
