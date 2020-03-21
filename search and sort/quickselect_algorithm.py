"""
Quickselect is a selection algorithm to find the k-th smallest element in
an unordered list. It is related to the quick sort sorting algorithm.
"""


def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pivot = partition(arr, l, r)
        print('pivot:{} kk:{} low:{} high:{} nums:{}'.format(
            pivot, k, l, r, arr))
        if pivot - l == k - 1:
            return arr[pivot]
        if pivot - l > k - 1:
            return kthSmallest(arr, l, pivot - 1, k)

        return kthSmallest(arr, pivot + 1, r,
                           k - pivot + l - 1)
    return None


if __name__ == '__main__':
    arr = [10, 4, 5, 8, 6, 11, 1, 1]
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    n = len(arr)
    k = 3
    k = 8
    print(kthSmallest(arr[:], 0, n - 1, k))
