class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int, vector<int>> m;
        for(int i = 0; i < manager.size(); ++i){
            if (manager[i] == -1) continue;
            m[manager[i]].push_back(i);
        }
        int ret = 0;
        deque<vector<int>> que;
        que.push_back({headID, informTime[headID]});
        while(!que.empty()){
            auto &f = que.front();
            int id = f[0], cnt = f[1];
            ret = max(ret, cnt);
            que.pop_front();
            for(auto &nxt: m[id]){
                que.push_back({nxt, cnt + informTime[nxt]});
            }
        }
        return ret;
    }
};