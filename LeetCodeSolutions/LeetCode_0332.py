class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency = collections.defaultdict(list)
        for a, b in tickets:
            adjacency[a].append(b)
        for i in adjacency:
            adjacency[i].sort(reverse=True)
        res = []

        def dfs(cur):
            while adjacency[cur]:
                dfs(adjacency[cur].pop())
            res.insert(0, cur)

        dfs('JFK')
        return res
