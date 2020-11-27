class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        s = set()
        for k, v in counter.items():
            if v not in s:
                s.add(v)
            else:
                return False
        return True
