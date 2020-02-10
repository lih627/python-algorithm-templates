class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words:
            return []
        res = []

        def search(s):
            ss = {
                'qwertyuiopQWERTYUIOP': 0,
                'asdfghjklASDFGHJKL': 1,
                'zxcvbnmZXCVBNM': 2
            }
            for k, v in ss.items():
                if s in k:
                    return v
            return -1

        for tmp in words:
            idx = 0
            flag = True
            start_line = search(tmp[idx])
            idx += 1
            while idx < len(tmp):
                cur_line = search(tmp[idx])
                if cur_line != start_line:
                    flag = False
                    break
                idx += 1
            if flag:
                res.append(tmp)
        return res
