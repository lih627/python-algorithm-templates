struct Node{
    int x, y, h;
    Node(int x_, int y_, int h_):x(x_), y(y_), h(h_){}
};

struct cmp{
    bool operator()(const Node &a, const Node &b) const{
        return a.h > b.h;
    }
};


class DSU{
private:
    vector<int> parents;
    int size;
public:
    DSU(int n):parents(n + 1), size(n){
        iota(parents.begin(), parents.end(), 0);
    }

    int find(int x){
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }

    void un(int x, int y){
        int rx = find(x), ry = find(y);
        if (rx != ry) parents[rx] = ry;
    }

    inline bool isConnected(int x, int y){return find(x) == find(y);}
};

int POS[51][51];
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        priority_queue<Node, vector<Node>, cmp> pq;
        for (int r = 0; r < row; ++r)
            for(int c = 0; c < col; ++c){
                POS[r][c] = r * row + c + 1;
                pq.emplace(r, c, grid[r][c]);
            }

        DSU dsu(row * col);
        int ret = 0;
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!dsu.isConnected(POS[0][0], POS[row - 1][col - 1])){
            auto node = pq.top();
            pq.pop();
            int x = node.x, y = node.y;
            ret = node.h;
            for(int i = 0; i < 4; ++i){
                int xx = x + dirs[i][0], yy = y + dirs[i][1];
                if (xx > -1 && xx < row && yy > -1 && yy < col && ret >= grid[xx][yy])
                    dsu.un(POS[xx][yy], POS[x][y]);
            }
        }
        return ret;
    }
};