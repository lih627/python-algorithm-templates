class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for idx, _ in enumerate(numbers):
            if target - _ not in d:
                d[_] = idx + 1
            else:
                return [d[target - _], idx + 1]
