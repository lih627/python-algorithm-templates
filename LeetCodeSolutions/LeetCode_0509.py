class Solution:
    def fib(self, N: int) -> int:
        memory = {0: 0, 1: 1}

        def helper(n):
            print(memory)
            if n in memory:
                return memory[n]
            tmp = helper(n - 1) + helper(n - 2)
            memory[n] = tmp
            return tmp

        return helper(N)
