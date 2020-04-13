import collections
import heapq
from typing import List

"""
LeetCode 743
迪杰特斯拉算法

空间复杂度
堆优化 O(ElogE)
原始 O(N^2 + E)
"""


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        """
        堆优化版本
        """
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))
        dist = [float('inf')] * (N + 1)
        dist[0] = -1
        visited = set()
        dist[K] = 0
        while len(visited) < N:
            select_vertex = -1
            init_dist = float('inf')
            for i in range(1, N + 1):
                if i not in visited and dist[i] < init_dist:
                    select_vertex = i
                    init_dist = dist[i]
            if select_vertex == -1:
                break
            visited.add(select_vertex)
            for v, w in graph.get(select_vertex, []):
                if w + init_dist < dist[v]:
                    dist[v] = w + init_dist
        if max(dist) == float('inf'):
            return -1
        return max(dist)
