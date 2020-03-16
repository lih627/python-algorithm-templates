class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        d = 1
        while self.stack and price >= self.stack[-1][0]:
            d += self.stack.pop()[1]
        self.stack.append([price, d])
        return d

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
