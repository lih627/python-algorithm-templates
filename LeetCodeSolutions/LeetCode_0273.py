class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        to9 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        to19 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                'Nineteen']
        to99 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        res = []

        def trans(n):
            ans = []
            if n // 100:
                ans.append(to9[n // 100 - 1])
                ans.append('Hundred')
            if 9 < n % 100 < 20:
                ans.append(to19[n % 100 - 10])
                return ans
            if n % 100 >= 20:
                ans.append(to99[n % 100 // 10 - 2])
            if n % 10:
                ans.append(to9[n % 10 - 1])
            return ans

        billion = num // 10 ** 9
        tmp = trans(billion)
        if tmp:
            res += tmp + ['Billion']
        million = num % 10 ** 9 // 10 ** 6
        tmp = trans(million)
        if tmp:
            res += tmp + ['Million']
        thousand = num % 10 ** 9 % 10 ** 6 // 10 ** 3
        tmp = trans(thousand)
        if tmp:
            res += tmp + ['Thousand']
        hundred = num % 10 ** 9 % 10 ** 6 % 10 ** 3
        tmp = trans(hundred)
        if tmp:
            res += tmp
        return ' '.join(res)
