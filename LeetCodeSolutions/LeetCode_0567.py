class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = [0 for i in range(26)]
        s2_cnt = s1_cnt[:]

        def trans(x):
            return ord(x) - ord('a')

        for i in s1:
            s1_cnt[trans(i)] += 1
        n_s1 = len(s1)
        for i in s2[:n_s1]:
            s2_cnt[trans(i)] += 1
        res = list(map(lambda x: x[0] - x[1], zip(s1_cnt, s2_cnt)))
        if not any(res):
            return True
        cur_idx = 1
        while cur_idx + n_s1 <= len(s2):
            res[trans(s2[cur_idx - 1])] += 1
            res[trans(s2[cur_idx + n_s1 - 1])] -= 1
            if not any(res):
                return True
            cur_idx += 1
        return False
