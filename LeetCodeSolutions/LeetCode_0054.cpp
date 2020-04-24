class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.empty()) return res;
        int row = matrix.size(), col = matrix[0].size();
        bool visited[row + 1][col + 1];
        for (int i = 0; i != row + 1; ++i){
            for (int j = 0; j != col + 1; ++j){
                if (i == row || j == col){
                    visited[i][j] = true;
                }
                else visited[i][j] = false;
            }
        }
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0, cnt = 0;
        int dx, dy;
        int xx, yy;
        for (int i = 0; i != row * col; ++i){
            res.push_back(matrix[x][y]);
            visited[x][y] = true;
            dx = dirs[cnt][0];
            dy = dirs[cnt][1];
            xx = dx + x;
            yy = dy + y;
            if (xx < 0 or yy < 0 or visited[xx][yy]){
                ++cnt;
                cnt %= 4;
                dx = dirs[cnt][0];
                dy = dirs[cnt][1];
                x += dx;
                y += dy;
            }
            else{
                x = xx;
                y = yy;
            }
        }
        return res;
    }
};