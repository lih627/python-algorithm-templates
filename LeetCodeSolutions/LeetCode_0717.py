class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        flag = False
        while (i < len(bits)):
            if bits[i] == 1:
                i += 2
            else:
                i += 1
                if i == len(bits):
                    flag = True
        return flag
