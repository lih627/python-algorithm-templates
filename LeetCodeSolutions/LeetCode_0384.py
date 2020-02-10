class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.org = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.org[:]
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for _ in range(len(self.array)):
            idx = random.randrange(_, len(self.array))
            self.array[_], self.array[idx] = self.array[idx], self.array[_]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
