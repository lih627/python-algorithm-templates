class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == x + y or z == x or z == y:
            return True
        visited = set()
        state = (0, 0)
        que = collections.deque()
        que.append(state)
        while que:
            xx, yy = que.popleft()
            visited.add((xx, yy))
            if xx + yy == z:
                return True
            if ((x, yy)) not in visited:
                que.append(((x, yy)))
            if ((xx, y)) not in visited:
                que.append((xx, y))
            if ((0, yy)) not in visited:
                que.append((0, yy))
            if ((xx, 0)) not in visited:
                que.append((xx, 0))
            if yy > 0:
                if x - xx <= yy:
                    nx, ny = x, yy - x + xx
                    if (nx, ny) not in visited:
                        que.append((nx, ny))
                else:
                    if (xx + yy, 0) not in visited:
                        que.append((xx + yy, 0))
            if xx > 0:
                if y - yy <= xx:
                    nx, ny = xx - y + yy, y
                    if (nx, ny) not in visited:
                        que.append((nx, ny))
                else:
                    if (0, xx + yy) not in visited:
                        que.append((0, xx + yy))

        return False

    def canMeasureWater_2(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
