class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        row, col = len(image), len(image[0])
        que = deque()
        que.append((sr, sc))
        visited = set((sr, sc))
        cur_color = image[sr][sc]
        if cur_color == newColor:
            return image
        image[sr][sc] = newColor

        def helper(_r, _c):
            if -1 < _r < row and -1 < _c < col and (_r, _c) not in visited:
                visited.add((_r, _c))
                if image[_r][_c] == cur_color:
                    image[_r][_c] = newColor
                    que.append((_r, _c))
            return None

        while que:
            r, c = que.pop()
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)
        return image
