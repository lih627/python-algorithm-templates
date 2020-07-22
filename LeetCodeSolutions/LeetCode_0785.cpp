class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        if(n == 0) return true;
        vector<bool> visited(n, false), isA(n, false), isB(n, false);
        for (int node = 0; node < n; ++node){
            if (visited[node]) continue;
            queue<int> que;
            isA[node] = true;
            que.push(node);
            // printf("cur___ node %d, %s\n", node, isA[node] ? "A": isB[node] ? "B": "None");
            while(!que.empty()){
                int node = que.front();
                // printf("cur node %d, %s\n", node, isA[node] ? "A": isB[node] ? "B": "None");
                que.pop();
                if (visited[node]) continue;
                visited[node] = true;
                if (isA[node]){
                    for(int neighbor: graph[node]){
                        // printf("nei node %d, %s\n", neighbor, isA[neighbor] ? "A": isB[neighbor] ? "B": "None");
                        if (isA[neighbor]) return false;
                        else{
                            isB[neighbor] = true;
                            visited[neighbor] = true;
                            // printf("nei node %d, %s\n", neighbor, isA[neighbor] ? "A": isB[neighbor] ? "B": "None");
                        for(auto tmp: graph[neighbor])
                                if(!visited[tmp]) {que.push(tmp); isA[tmp]=true;};
                        }
                    }
                }
                else{
                    for(int neighbor: graph[node]){
                        // printf("nei node %d, %s\n", neighbor, isA[neighbor] ? "A": isB[neighbor] ? "B": "None");
                        if (isB[neighbor]) return false;
                        else{
                            isA[neighbor] = true;
                            visited[neighbor] = true;
                            // printf("nei node %d, %s\n", neighbor, isA[neighbor] ? "A": isB[neighbor] ? "B": "None");
                        for(auto tmp: graph[neighbor])
                                if(!visited[tmp]) {que.push(tmp); isB[tmp] = true;}
                        }
                    }
                }
            }
        }
        return true;
    }
};