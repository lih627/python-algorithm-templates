class Solution {
public:
    vector<int> parents;
    int size;
    int find(int x){
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }
    bool un(int x, int y){
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        parents[rx] = ry;
        return true;
    }

    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        parents.resize(n + 1, 0);
        iota(parents.begin(), parents.end(), 0);
        int size = n;
        vector<vector<int>> a, b, c;
        for(auto &e: edges){
            if(e[0] == 1) a.push_back({e[2], e[1]});
            else if(e[0] == 2) b.push_back({e[2], e[1]});
            else c.push_back({e[2], e[1]});
        }
        int ret = 0;
        for(auto &e: c){
            if (un(e[0], e[1])) --size;
            else ++ret;
        }
        int tmp = size;
        vector<int> tparents(parents.begin(), parents.end());
        for(auto &e: a){
            if (un(e[0], e[1])) --size;
            else ++ret;
        }
        if (size > 1) return -1;
        size = tmp;
        parents = tparents;
        for(auto &e: b){
            if (un(e[0], e[1])) --size;
            else ++ret;
        }
        return size == 1? ret: -1;
    }
};