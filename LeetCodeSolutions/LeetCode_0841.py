import collections


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)
        que = collections.deque()
        que.append(0)
        visited.add(0)
        while que:
            _r = que.popleft()
            for _room in rooms[_r]:
                if _room not in visited:
                    visited.add(_room)
                    que.append(_room)
        return len(visited) == n
