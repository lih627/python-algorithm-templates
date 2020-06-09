class Solution {
public:
    bool oneEditAway(string first, string second) {
        int m = first.size();
        int n = second.size();
        if (abs(m - n) > 1) return false;
        vector<vector<int> > dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i <= m; ++i){
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; ++j){
            dp[0][j] = j;
        }
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j){
                if (first[i - 1] == second[j - 1]) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = min(dp[i  - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1])) + 1;
            }
        return dp[m][n] < 2;
    }
};