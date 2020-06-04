class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = []
        n = len(arr)
        for idx, val in enumerate(arr):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val ^ prefix[-1])
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    tmp = prefix[k] ^ prefix[j - 1]
                    if i == 0:
                        if prefix[j - 1] == tmp:
                            ans += 1
                    else:
                        if prefix[j - 1] ^ prefix[i - 1] == tmp:
                            ans += 1
        return ans
