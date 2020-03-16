class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        if n == 1:
            return [0]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        leaves = [i for i in graph if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            tmp = []
            for leaf in leaves:
                node = graph[leaf].pop()
                graph[node].remove(leaf)
                if len(graph[node]) == 1:
                    tmp.append(node)
            leaves = tmp
        return leaves
