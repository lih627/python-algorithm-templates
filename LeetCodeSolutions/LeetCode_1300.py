class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        diff = target
        num = 0
        idx = -1
        presum = 0
        ret = 0
        while idx < len(arr) - 1:
            num += 1
            while arr[idx + 1] <= num:
                idx += 1
                presum += arr[idx]
                if idx == len(arr) - 1:
                    break
            cur_diff = abs(target - presum - num * (len(arr) - idx - 1))
            if cur_diff < diff:
                ret = num
                diff = cur_diff
            else:
                break
        return ret
