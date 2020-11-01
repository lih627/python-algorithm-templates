class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.nums = []
        i, j = 0, 0
        for k in range(len(v1) + len(v2)):
            if k & 1:
                if j < len(v2):
                    self.nums.append(v2[j])
                    j += 1
                else:
                    self.nums.append(v1[i])
                    i += 1
            else:
                if i < len(v1):
                    self.nums.append(v1[i])
                    i += 1
                else:
                    self.nums.append(v2[j])
                    j += 1
        self.cur = 0
        # print(self.nums)

    def next(self) -> int:
        tmp = self.nums[self.cur]
        self.cur += 1
        return tmp

    def hasNext(self) -> bool:
        return self.cur < len(self.nums)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
