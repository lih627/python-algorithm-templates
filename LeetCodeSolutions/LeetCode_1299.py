class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                premax = arr[i]
                arr[i] = -1
            else:
                cmax = max(premax, arr[i])
                arr[i] = premax
                premax = cmax
        return arr
