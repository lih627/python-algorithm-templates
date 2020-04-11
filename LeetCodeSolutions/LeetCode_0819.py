class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        strs = []
        tmp = ''
        for s in paragraph:
            if s in '!? \';.,':
                if tmp:
                    strs.append(tmp)
                    tmp = ''
            else:
                tmp += s.lower()
        if tmp:
            strs.append(tmp)
        cnt = {}
        max_num = 0
        res = ''
        banned = set(banned)
        for string in strs:
            if string not in banned:
                if string not in cnt:
                    cnt[string] = 1
                else:
                    cnt[string] += 1
                if cnt[string] > max_num:
                    max_num = cnt[string]
                    res = string
        return res
