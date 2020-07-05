bool cmp(vector<int> &a, vector<int> &b){
    return a[2] < b[2];
}

class DSU{
    public:
    vector<int> parent;
    DSU(int n){
        parent.resize(n + 1);
        for(int i = 0;  i < n + 1; ++i) parent[i] = i;
    }

    int find(int x){
        if (parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void _union(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if (rx != ry){
            parent[rx] = ry;
        }
    }

    bool isCircle(int x, int y){
        return find(x) == find(y);
    }

};

class Solution {
public:
    int minimumCost(int N, vector<vector<int>>& connections) {
        sort(connections.begin(), connections.end(), cmp);
        DSU dsu(N);
        int cnt = 0;
        int ret = 0;
        for(auto& edges: connections){
            if(dsu.isCircle(edges[0], edges[1])) continue;
            else{
                dsu._union(edges[0], edges[1]);
                ret += edges[2];
                ++cnt;
            }
            if (cnt == N - 1) break;
        }
        return cnt == N - 1? ret: -1;

    }
};