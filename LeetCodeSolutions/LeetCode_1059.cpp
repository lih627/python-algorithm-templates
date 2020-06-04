class Solution {
    vector<bool> valid;
    vector<bool> visited;
    unordered_map<int, vector<int> > adjacency;

public:
    bool leadsToDestination(int n, vector<vector<int>>& edges, int source, int destination) {
        valid.resize(n, false);
        visited.resize(n, false);
        for (auto edge: edges)
            adjacency[edge[0]].push_back(edge[1]);
        return dfs(source, destination);
    }

    bool dfs(int cur, int des){
        if (cur == des){
            if (adjacency[des].empty()) return true;
            else return false;
        }
        if (adjacency[cur].empty()) return false;
        for (auto node: adjacency[cur]){
            if (visited[node]) return false;
            if (valid[node]) return true;
            visited[node] = true;
            if(!dfs(node, des)) return false;
            visited[node] = false;
        }
        valid[cur] = true;
        return true;
    }

};