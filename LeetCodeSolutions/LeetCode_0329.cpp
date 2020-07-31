vector<vector<int> > dirs{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int ans = 0;
        int row = matrix.size();
        if (row == 0) return 0;
        int col = matrix[0].size();
        vector<vector<int>> memo(row, vector<int>(col, 0));
        for (int i = 0; i < matrix.size(); ++i)
            for(int j = 0; j < matrix[0].size(); ++j)
                ans = max(ans, dp(i, j, matrix, memo));
        return ans;
    }

    int dp(int i, int j, vector<vector<int>> &matrix, vector<vector<int>> &memo){
        if (memo[i][j]) return memo[i][j];
        int ret = 1, row = matrix.size(), col = matrix[0].size();
        for (auto dir: dirs){
            int dx = dir[0];
            int dy = dir[1];
            int xx = i + dx, yy = j + dy;
            if (xx > -1 && xx < row && yy > -1 && yy < col){
                if (matrix[xx][yy] > matrix[i][j])
                    ret = max(ret, 1 + dp(xx, yy, matrix, memo));
            }
        }
        memo[i][j] = ret;
        return ret;
    }
};