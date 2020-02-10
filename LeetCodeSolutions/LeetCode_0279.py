class Solution:
    def numSquares(self, n: int) -> int:
        from queue import Queue
        que = Queue()
        que.put((n, 0))
        while True:
            n, step = que.get()
            step += 1
            for _ in range(int(math.sqrt(n)), 0, -1):
                if _ * _ < n:
                    que.put((n - _ * _, step))
                elif _ * _ == n:
                    return step
