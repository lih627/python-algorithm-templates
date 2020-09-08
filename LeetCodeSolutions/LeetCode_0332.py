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


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ret = []

        def dfs(cur):
            while graph[cur]:
                nxt = heapq.heappop(graph[cur])
                dfs(nxt)
            ret.append(cur)

        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        for key in graph:
            heapq.heapify(graph[key])
        dfs('JFK')
        return ret[::-1]
