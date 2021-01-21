class DistanceLimitedPathsExist {
    vector<int> parents;
    bool visited[10010];
    int dep[10010], fa[10010], pre[10010][15], dis[10010][15];

    int find(int x){
        if(parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    bool un(int x, int y){
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        parents[rx] = ry;
        return true;
    }

    void dfs(int node, int prev, vector<vector<pair<int, int>>> &graph, int w, int depth){
        visited[node] = true;
        dep[node] = depth;
        if (prev != -1){
            pre[node][0] = prev;
            dis[node][0] = w;
        }
        for(pair<int, int> &nxt: graph[node]){
            int nex = nxt.first, edgeDis = nxt.second;
            if (!visited[nex]){
                dfs(nex, node, graph, edgeDis, depth + 1);
            }
        }
    }

public:
    DistanceLimitedPathsExist(int n, vector<vector<int>>& edgeList) {
        parents.resize(n);
        iota(parents.begin(), parents.end(), 0);
        memset(visited, false, sizeof(visited));
        memset(dep, 0, sizeof(dep));
        memset(fa, -1, sizeof(fa));
        memset(pre, -1, sizeof(pre));
        memset(dis, 0, sizeof(dis));

        // kruskal
        vector<vector<pair<int, int>>> graph(n);
        sort(edgeList.begin(), edgeList.end(), [](const vector<int> &a, const vector<int> &b){return a[2] < b[2];});
        for(auto &edge: edgeList){
            int x = edge[0], y = edge[1], dis = edge[2];
            if (un(x, y)) {
                graph[x].emplace_back(y, dis);
                graph[y].emplace_back(x, dis);
            }
        }

        // generate depth, fa, pre[n][0], dis[n][0]
        for(int node = 0; node < n; ++node){
            if (!visited[node])
                dfs(node, -1, graph, 0, 0);
        }

        // compute pre, dis
        for(int i = 1; (1 << i) < n; ++i)
            for(int node = 0; node < n; ++ node){
                if (pre[node][i - 1] == -1) continue;
                pre[node][i] = pre[pre[node][i - 1]][i - 1];
                if(pre[node][i] != -1) dis[node][i] = max(dis[node][i - 1], dis[pre[node][i - 1]][i - 1]);
            }
    }

    bool query(int p, int q, int limit) {
        if (find(p) != find(q)) return false;
        int dp = dep[p], dq = dep[q];
        if (dp > dq){
            swap(dp, dq);
            swap(p, q);
        }
        // dq < dq
        int max_dis = 0;
        int delta = dq - dp;
        for(int i = 0; (1 << i) <= delta; ++i){
            if (delta & (1 << i)) {
                max_dis = max(max_dis, dis[q][i]);
                q = pre[q][i];
            }
        }

        for(int i = 14; i >= 0; --i){
            if (pre[q][i] != pre[p][i]){
                max_dis = max(max_dis, max(dis[p][i], dis[q][i]));
                if (max_dis >= limit) break;
                q = pre[q][i];
                p = pre[p][i];
            }
        }
        if (p != q) max_dis = max(max_dis, max(dis[p][0], dis[q][0]));
        return max_dis < limit;
    }
};

/**
 * Your DistanceLimitedPathsExist object will be instantiated and called as such:
 * DistanceLimitedPathsExist* obj = new DistanceLimitedPathsExist(n, edgeList);
 * bool param_1 = obj->query(p,q,limit);
 */