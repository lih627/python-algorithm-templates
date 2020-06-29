class Solution {
public:
    unordered_map<string, unordered_map<string, double> > graph;
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries){
        int n = equations.size();
        for(int i = 0; i < n; ++i){
            string a = equations[i][0], b = equations[i][1];
            graph[a][b] = values[i];
            graph[b][a] = 1.0 / values[i];
        }
        vector<double> ret;
        for(auto pairs: queries){
            ret.push_back(bfs(pairs[0], pairs[1]));
        }
        return ret;
    }

    double bfs(string a, string b){
        if(graph.count(a) == 0 || graph.count(b) == 0) return -1;
        if(a == b) return 1.0;
        typedef pair<string, double> PSD;
        queue<PSD> q;
        unordered_set<string> visited;
        visited.insert(a);
        q.push(make_pair(a, 1.0));
        while(!q.empty()){
            auto p = q.front();
            q.pop();
            for (auto tmp: graph[p.first]){
                if(visited.count(tmp.first) == 0){
                    double val = tmp.second * p.second;
                    graph[a][tmp.first] = val;
                    graph[tmp.first][a] = 1 / val;
                    if(tmp.first == b) return val;
                    q.push(make_pair(tmp.first, val));
                }
            }
        }
        return -1.0;

    }
};