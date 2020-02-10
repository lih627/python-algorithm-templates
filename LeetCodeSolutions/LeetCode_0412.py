class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if not n: return []
        res = []
        d = {3: 'Fizz', 5: 'Buzz'}
        for _ in range(1, n + 1):
            tmp = ''
            for key in d:
                if _ % key == 0:
                    tmp += d[key]
            if not tmp:
                tmp = str(_)
            res.append(tmp)
        return res
