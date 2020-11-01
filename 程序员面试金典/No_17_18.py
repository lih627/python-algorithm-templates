from collections import Counter


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        counter = Counter(small)
        ret = []
        cnt = 0
        l, r = 0, 0
        for r in range(len(big)):
            if big[r] in counter:
                if counter[big[r]] == 1:
                    cnt += 1
                counter[big[r]] -= 1
            if cnt == len(small):
                while big[l] not in counter or counter[big[l]] != 0:
                    if big[l] in counter:
                        counter[big[l]] += 1
                    l += 1
                if ret == [] or r - l < ret[1] - ret[0]:
                    ret = [l, r]
                counter[big[l]] += 1
                cnt -= 1
                l += 1
        return ret
