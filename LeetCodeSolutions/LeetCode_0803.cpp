class DSU{
private:
    vector<int> parents;
    vector<int> sz;
    int size;
public:
    DSU(int n):parents(n + 1), sz(n + 1, 1), size(n){
        iota(parents.begin(), parents.end(), 0);
    }

    int find(int x){
        if(parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    void un(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if (rx == ry) return;
        if(ry == size) swap(rx, ry);
        parents[ry] = rx;
        sz[rx] += sz[ry];
    }

    inline int un_size(){return sz[size];}

    void print(){
        cout << "parents: " << endl;
        for(auto t: parents) cout << t << ' '; cout << endl;
        cout << "sz: " << endl;
        for(auto t: sz)  cout << t << ' '; cout << endl;
    }
};


bool hitsmap[210][210];
int dirs[4][2] = {{-1 ,0}, {1, 0}, {0, 1}, {0, -1}};

class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        int n = hits.size();
        int row = grid.size(), col = grid[0].size();
        memset(hitsmap, 0, sizeof(hitsmap));
        for(auto h: hits){
            hitsmap[h[0]][h[1]] = true;
        }
        DSU dsu(row * col);
        for(int c = 0; c < col; ++c){
            if (!hitsmap[0][c] && grid[0][c] == 1) dsu.un(c, row * col);
        }
        for(int r = 1; r < row; ++r){
            for(int c = 0; c < col; ++c){
                if(!hitsmap[r][c] && grid[r][c] == 1){
                    for(int tmp = 0; tmp < 4; ++tmp){
                        int x = r + dirs[tmp][0], y = c + dirs[tmp][1];
                        if (-1 < x && x < row && -1 < y && y < col && grid[x][y] == 1 && !hitsmap[x][y]){
                            dsu.un(r * col + c, x * col + y);
                        }
                    }
                }
            }
        }
        vector<int> ans(n, 0);
        for(int i = n - 1; i > -1; --i){
            int cx = hits[i][0], cy = hits[i][1];
            hitsmap[cx][cy] = false;
            if (grid[cx][cy] == 0) continue;
            int before = dsu.un_size();
            if (cx == 0) dsu.un(cy, row * col);
            for(int t = 0; t < 4; ++ t){
                int x = cx + dirs[t][0], y = cy + dirs[t][1];
                if (-1 < x && x < row && -1 < y && y < col && grid[x][y] == 1 && !hitsmap[x][y]){
                    dsu.un(cx * col + cy, x * col + y);
                }
            }
            int tmp = dsu.un_size() - before - 1;
            ans[i] = max(tmp, 0);
        }
        return ans;
    }
};