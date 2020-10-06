class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        isneg = numerator * denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator // denominator
        numerator -= integer * denominator
        if numerator == 0:
            if isneg:
                return '-' + str(integer)
            return str(integer)
        d = {}
        floats = []
        div = numerator * 10
        while div not in d:
            d[div] = len(floats)
            ret = div // denominator
            floats.append(str(ret))
            div -= ret * denominator
            div *= 10
            if div == 0:
                if isneg:
                    return '-' + str(integer) + '.' + ''.join(floats)
                return str(integer) + '.' + ''.join(floats)
        ret = str(integer) + '.'
        i = 0
        ret += ''.join(floats[:d[div]])
        ret += '(' + ''.join(floats[d[div]:]) + ')'
        if isneg:
            return '-' + ret
        return ret
