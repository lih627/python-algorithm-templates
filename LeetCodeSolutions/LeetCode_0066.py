class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                if digits[i] == 9:
                    plus = True
                    ans.append(0)
                else:
                    ans.append(digits[i] + 1)
                    plus = False
            else:
                if plus:
                    if digits[i] == 9:
                        plus = True
                        ans.append(0)
                    else:
                        plus = False
                        ans.append(digits[i] + 1)
                else:
                    ans.append(digits[i])
        if plus:
            ans.append(1)
        return ans[::-1]
