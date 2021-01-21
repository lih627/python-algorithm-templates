class Solution {
    int dis, node;
public:
    int treeDiameter(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> adj[n + 1];
        bool vis[n + 1];
        memset(vis, false, sizeof(vis));
        dis = 0;
        node = 0;
        for(auto e: edges){
            adj[e[0]].emplace_back(e[1]);
            adj[e[1]].emplace_back(e[0]);
        }
        vis[0] = true;
        dfs(0, 0, adj, vis);
        memset(vis, false, sizeof(vis));
        vis[node] = true;
        dfs(node, 0, adj, vis);
        return dis - 1;
    }

    void dfs(int n, int d, vector<int> adj[], bool *vis){
        d += 1;
        // cout << "node " << n << " dis " << d << endl;
        // for (int i = 0; i < 5; ++i) cout << vis[i] << ' '; cout << endl;
        if (d > dis) {dis = d; node = n;}
        for(auto &nxt: adj[n]){
            if (!vis[nxt]) {
                vis[nxt] = true;
                dfs(nxt, d, adj, vis);
            }
        }
    }
};