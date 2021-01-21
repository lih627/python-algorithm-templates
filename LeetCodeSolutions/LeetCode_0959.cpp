class DSU{
    private:
        vector<int> parents;
        int size;
        int regions;
    public:
    DSU(int n):parents(n + 1), size(n + 1), regions(n){
        iota(parents.begin(), parents.end(), 0);
    }

    int find(int x){
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    bool un(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if (rx == ry) return false;
        --regions;
        parents[rx] = ry;
        return true;
    }

    int cnt(){return regions;}
};
struct VectorHasher {
    int operator()(const vector<int> &V) const {
        int hash =0;
        for(auto &i : V) {
            hash = hash * 100 + i;
        }
        return hash;
    }
};

class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        unordered_map<vector<int>, int, VectorHasher> mp;
        int c = 1;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                for(int k = 0; k < 4; ++k) mp[{i, j, k}] = c ++;
        DSU dsu(4 * n * n);
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j){
                auto s = grid[i][j];
                if (s == '\\'){
                    dsu.un(mp[{i, j, 1}], mp[{i, j, 2}]);
                    dsu.un(mp[{i, j, 0}], mp[{i, j, 3}]);
                }
                else if (s == '/'){
                    dsu.un(mp[{i, j, 1}], mp[{i, j, 0}]);
                    dsu.un(mp[{i, j, 2}], mp[{i, j, 3}]);
                }
                else{
                    dsu.un(mp[{i, j, 0}], mp[{i, j, 1}]);
                    dsu.un(mp[{i, j, 2}], mp[{i, j, 3}]);
                    dsu.un(mp[{i, j, 1}], mp[{i, j, 2}]);
                }
                if (mp.count({i, j - 1, 2})) dsu.un(mp[{i, j, 0}], mp[{i, j - 1, 2}]);
                if (mp.count({i, j + 1, 0})) dsu.un(mp[{i, j, 2}], mp[{i, j + 1, 0}]);
                if (mp.count({i - 1, j, 3})) dsu.un(mp[{i - 1, j, 3}], mp[{i, j, 1}]);
                if (mp.count({i + 1, j, 1})) dsu.un(mp[{i + 1, j, 1}], mp[{i, j, 3}]);
            }

        return dsu.cnt();
    }
};