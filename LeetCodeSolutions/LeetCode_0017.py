from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        elems = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def backtrace(tmp, rest):
            if not rest:
                res.append(tmp)
                return
            cur_dig = rest[0]
            for _ in elems[cur_dig]:
                backtrace(tmp + _, rest[1:])

        backtrace('', digits)
        return res
