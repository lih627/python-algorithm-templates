class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.nums = collections.defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.nums:
            if value - key in self.nums:
                if value - key == key:
                    if self.nums[key] > 1:
                        return True
                else:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
