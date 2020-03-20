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

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        类似快速选择思路
        """
        nums = arr
        if k == 0:
            return []
        if len(arr) <= k:
            return arr

        def partition_slow(low, high):
            x = nums[low]
            i = high + 1

            for j in range(high, low, -1):
                if nums[j] > x:
                    i -= 1
                    nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            nums[i], nums[low] = nums[low], nums[i]
            return i

        def partition_fast(lo, hi):
            nonlocal nums
            v = nums[lo]
            i = lo

            for j in range(lo + 1, hi + 1):
                if nums[j] < v:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[i], nums[lo] = nums[lo], nums[i]
            return i

        n = len(arr)
        low, high = 0, n - 1
        kk = k
        partition = partition_fast
        while kk > 0 and kk <= high - low + 1:
            pivot = partition(low, high)
            # print('pivot:{} kk:{} low:{} high:{} nums:{}'.format(
            #     pivot, kk, low, high, nums))
            if pivot - low == kk - 1:
                break
            elif pivot - low > kk - 1:
                high = pivot - 1
            else:
                kk = kk - pivot + low - 1
                low = pivot + 1
        return nums[:k]
