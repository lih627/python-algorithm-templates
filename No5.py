from collections import defaultdict


def _compute_dis(start, end, graph):
    ret = {}
    # ret[start] = 0
    l, r = min(start, end), max(start, end)
    while l <= r:
        if l == start:
            ret[l] = 0
        else:
            ret[l] = float('inf')
        l += 1
    # print(ret)
    visited_edges = set()
    while ret[end] == float('inf'):
        st, en, d = -1, -1, float('inf')
        for cur_node in ret:
            if ret[cur_node] != float('inf'):
                for nxt in graph[cur_node]:
                    if (cur_node, nxt) in visited_edges:
                        continue
                    if ret[cur_node] + graph[cur_node][nxt] < d:
                        d = ret[cur_node] + graph[cur_node][nxt]
                        st = cur_node
                        en = nxt

        visited_edges.add((st, en))
        # if en in ret:
        ret[en] = min(d, ret[en])
        # else:
        #     ret[en] = d
    return ret


def solve(n, m, T, graph):
    dis1 = _compute_dis(1, n, graph)
    dis2 = _compute_dis(n, 1, graph)
    each_cycle = dis1[n] + dis2[1]
    print(each_cycle * T)


if __name__ == '__main__':
    n, m, T = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(m):
        x, y, d = map(int, input().split())
        graph[x][y] = d
    solve(n, m, T, graph)
