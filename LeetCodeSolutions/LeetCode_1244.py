class Leaderboard:

    def __init__(self):
        self.board = dict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = score
        else:
            self.board[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted([v for k, v in self.board.items()], reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
