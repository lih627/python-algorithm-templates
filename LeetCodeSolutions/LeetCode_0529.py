class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        states = collections.defaultdict(int)
        row, col = len(board), len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'M' or board[i][j] == 'B':
                    states[(i, j)] = -1
                elif board[i][j] == 'E':
                    cnt = 0
                    for dx, dy in dirs:
                        xx = i + dx
                        yy = j + dy
                        if -1 < xx < row and -1 < yy < col and board[xx][yy] == 'M':
                            cnt += 1
                    states[(i, j)] = cnt
        que = collections.deque()
        que.append(click)
        visited = set()
        visited.add(tuple(click))
        while que:
            i, j = que.popleft()
            if states[(i, j)] > 0:
                board[i][j] = str(states[(i, j)])
                break
            elif states[(i, j)] < 0:
                if board[i][j] == 'M':
                    board[i][j] = 'X'
                    break
            else:
                board[i][j] = 'B'
            for dx, dy in dirs:
                ii = i + dx
                jj = j + dy
                if -1 < ii < row and -1 < jj < col and (ii, jj) not in visited:
                    visited.add((ii, jj))
                    if '0' <= board[ii][jj] <= '9':
                        continue
                    if states[(ii, jj)] == -1:
                        continue
                    elif states[(ii, jj)] > 0:
                        board[ii][jj] = str(states[(ii, jj)])
                    else:
                        board[ii][jj] = 'B'
                        que.append([ii, jj])
        return board
