class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        mins = [0] * len(nums)
        stack = []
        curr_min = nums[0]
        for j in range(len(nums)):
            if nums[j] > curr_min:
                mins[j] = curr_min
            else:
                curr_min = nums[j]
                mins[j] = curr_min
        stack.append(float('inf'))

        print(nums)
        for j in range(len(nums) - 1, -1, -1):
            if stack[-1] <= mins[j]:
                while stack[-1] <= mins[j]:
                    stack.pop()
            #        print('1',j,stack)
            if stack[-1] >= nums[j]:
                stack.append(nums[j])
                #    print('2',j,stack)
                continue
            if nums[j] > stack[-1] > mins[j]:
                return True
        return False
