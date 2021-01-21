class DSU{
    vector<int> fa;
    vector<int> sz;
    int n;
    public:
    DSU(int _n): n(_n + 1), fa(_n + 1, 0), sz(_n + 1, 1){
        iota(fa.begin(), fa.end(), 0);
    }

    int find(int x){
        return fa[x] == x? x: fa[x] = find(fa[x]);
    }

    bool un(int x, int y){
        int rx = find(x), ry = find(y);
        if (rx == ry){
            return false;
        }
        if (sz[rx] < sz[ry]){
            swap(rx, ry);
        }
        sz[rx] += sz[ry];
        fa[ry] = rx;
        return true;
    }

    bool cnc(int x, int y){return find(x) == find(y);}

    void p(){
        for (auto c: fa) cout << c << ' '; cout << endl;
    }
};

class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        DSU dsu(n);
        int nq = queries.size();
        vector<int> index(nq);
        iota(index.begin(), index.end(), 0);
        sort(index.begin(), index.end(), [&](int i, int j){
            return queries[i][2] < queries[j][2];
        });
        auto f = [&](const vector<int> &a, const vector<int> & b) -> bool{
            return a[2] < b[2];
        };
        sort(queries.begin(), queries.end(), f);
        sort(edgeList.begin(), edgeList.end(), f);
        int k = 0;
        vector<bool> ret(nq, false);
        for(int i = 0; i < nq; ++i){
            int l = queries[i][2];
            while(k < edgeList.size() && edgeList[k][2] < l){
                dsu.un(edgeList[k][0], edgeList[k][1]);
                ++k;
            }
            // cout << "limit " << l;
            // cout << "fa ";
            // dsu.p();
            ret[index[i]] = dsu.cnc(queries[i][0], queries[i][1]);
        }
        return ret;
    }
};