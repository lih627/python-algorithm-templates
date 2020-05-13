class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [t.split(',') + [idx] for idx, t in enumerate(transactions)]
        res = []
        for i, val in enumerate(trans):
            if int(val[2]) > 1000:
                res.append(transactions[i])
                continue
            for j, vval in enumerate(trans):
                if i == j:
                    continue
                if val[0] == vval[0] and val[3] != vval[3] and abs(int(val[1]) - int(vval[1])) <= 60:
                    res.append(transactions[i])
                    break
        return res
