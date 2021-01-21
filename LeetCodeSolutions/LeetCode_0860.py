class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = collections.defaultdict(int)
        for bill in bills:
            d[bill] += 1
            if bill == 5:
                continue
            elif bill == 10:
                if d[5] >= 1:
                    d[5] -= 1
                else:
                    return False
            else:
                if d[10] >= 1 and d[5] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                else:
                    if d[5] >= 3:
                        d[5] -= 3
                    else:
                        return False
        return True
