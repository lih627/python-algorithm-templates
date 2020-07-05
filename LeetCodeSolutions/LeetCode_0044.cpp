class Solution {
public:
    bool isMatch(string s, string p) {
        int m = p.size(), n = s.size();
        vector<vector<bool> > dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        for(int i = 1; i < m + 1; ++i){
            if (p[i - 1] == '*') dp[i][0] = dp[i - 1][0];
        }

        for(int i = 1; i < m + 1; ++i)
            for(int j = 1; j < n + 1; ++j){
                if(p[i - 1] == '?') dp[i][j] = dp[i - 1][j - 1];
                else if(p[i - 1] == '*') dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                else if(p[i - 1] == s[j - 1]) dp[i][j] = dp[i - 1][j - 1];

                // printf("%d %d %s\n", i, j, dp[i][j]? "True": "False");
            }
        return dp[m][n];
    }
};