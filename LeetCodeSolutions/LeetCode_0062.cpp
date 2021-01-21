int dp[110][110];
class Solution {
public:
    int uniquePaths(int m, int n) {
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int r = 0; r < m; ++r){
            for(int c = 0; c < n; ++c){
                int u = r > 0? dp[r - 1][c]: 0;
                int l = c > 0? dp[r][c - 1]: 0;
                dp[r][c] += u + l;
            }
        }
        return dp[m - 1][n - 1];
    }
};