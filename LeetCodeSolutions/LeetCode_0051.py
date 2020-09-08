#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = set()
        queen_pos = []

        def helper(idx, ret):
            if idx == n:
                queen_pos.append(ret[:])
                return
            for col in range(n):
                if (idx, col) not in visited:
                    cur_pos = [(idx, col)]
                    visited.add((idx, col))
                    for [dx, dy] in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
                        cx, cy = idx + dx, col + dy
                        while -1 < cx < n and -1 < cy < n:
                            if (cx, cy) not in visited:
                                visited.add((cx, cy))
                                cur_pos.append((cx, cy))
                            cx += dx
                            cy += dy
                    ret.append(col)
                    helper(idx + 1, ret)
                    ret.pop()
                    while cur_pos:
                        visited.remove(cur_pos.pop())

        helper(0, [])
        # n_ret = len(queenpos)
        ret = []
        for cols in queen_pos:
            tmp = []
            for idx in cols:
                s = ''
                for i in range(n):
                    if i == idx:
                        s += 'Q'
                    else:
                        s += '.'
                tmp.append(s)
            ret.append(tmp)
        return ret

# @lc code=end
