class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr: return []

        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] < arr[largest]:
                largest = l
            if r < n and arr[r] < arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        # build
        for i in range(n // 2, -1, -1):
            heapify(arr, n, i)
        res = []
        idx = n - 1
        while k:
            res.append(arr[0])
            arr[0] = arr[idx]
            heapify(arr, idx, 0)
            idx -= 1
            k -= 1
        return res
