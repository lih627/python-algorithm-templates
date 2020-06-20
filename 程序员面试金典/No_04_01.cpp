class Solution {
    unordered_map<int, unordered_set<int> > graphs;
public:
    bool findWhetherExistsPath(int n, vector<vector<int>>& graph, int start, int target) {
        unordered_set<int> visited;
        for(auto v: graph){
            graphs[v[0]].insert(v[1]);
        }
        //bfs
        queue<int> que;
        que.push(start);
        visited.insert(start);
        if(start == target) return true;
        while(!que.empty()){
            int node = que.front();
            que.pop();
            for(auto n: graphs[node]){
                if(!visited.count(n)){
                    visited.insert(n);
                    if(n == target) return true;
                    que.push(n);
                }
            }
        }
        return false;
    }
};