class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = [idx for idx, val in enumerate(hasApple) if val]
        d = collections.defaultdict(int)
        for edge in edges:
            i, j = edge
            if i > j:
                d[i] = j
            else:
                d[j] = i
        visited = set()
        visited.add(0)
        ans = 0
        for node in nodes:
            while node not in visited:
                parent = d[node]
                ans += 2
                visited.add(node)
                node = parent
        return ans
