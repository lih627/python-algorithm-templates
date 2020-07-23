class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<int> dp(n, 0);
        for(int i = 0; i < n; ++i){
            dp[i] = i == 0? grid[0][i] : dp[i - 1] + grid[0][i];
        }
        for (int i = 1; i < m; ++i){
            for (int j = 0; j < n; ++j){
                dp[j] = j == 0? dp[j] + grid[i][j] : min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
};