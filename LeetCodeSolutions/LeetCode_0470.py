# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return (num - 1) // 4 + 1
            num = (num - 41) * 7 + rand7()
            if num <= 60:
                return (num - 1) // 6 + 1
            num = (num - 61) * 7 + rand7()
            if num <= 20:
                return (num - 1) // 2 + 1
