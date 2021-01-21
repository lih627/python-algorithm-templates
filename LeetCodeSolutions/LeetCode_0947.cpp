class DSU{
    private:
        vector<int> parents;
        int size;
        int region;
    public:
    DSU(int n): parents(n + 1), size(n + 1), region(n){
        iota(parents.begin(), parents.end(), 0);
    }

    int find(int x){
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }
    bool un(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if(rx == ry) return false;
        --region;
        parents[rx] = ry;
        return true;
    }

    int cnt(){return region;}
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int cnt = 0;
        unordered_map<int, int> mp;
        unordered_map<int, vector<int>> r, c;
        for(auto t: stones){
            int i = t[0], j = t[1];
            int hash = i * 10000 + j;
            mp[hash] = ++cnt;
            r[i].push_back(hash);
            c[j].push_back(hash);
        }
        DSU dsu(cnt);
        for(auto x: r){
            auto t = x.second;
            if(t.empty()) continue;
            int tmp = t[0];
            for(int i = 1; i < t.size(); ++i) dsu.un(mp[tmp], mp[t[i]]);
        }

        for(auto x: c){
            auto t = x.second;
            if(t.empty()) continue;
            int tmp = t[0];
            for(int i = 1; i < t.size(); ++i) dsu.un(mp[tmp], mp[t[i]]);
        }
        return cnt - dsu.cnt();
    }
};