class DSU{
    vector<int> parents;
    int size, circle;
public:
    DSU(int _sz){
        parents.resize(_sz + 1);
        for (int i = 1; i <= _sz; ++i) parents[i] = i;
        size = _sz;
        circle = _sz;
    }

    int find(int x){
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    void un(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if (rx != ry){
            parents[rx] = ry;
            --circle;
        }
    }

    bool isValid(){return circle == 1;}
};

class Solution {
public:
    int earliestAcq(vector<vector<int>>& logs, int N) {
        DSU dsu(N);
        sort(logs.begin(), logs.end());
        for(auto &v: logs){
            int t = v[0], a = v[1], b = v[2];
            dsu.un(a, b);
            if (dsu.isValid()) return t;
        }
        return -1;
    }
};