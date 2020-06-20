class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool> > dp(n + 1, vector<bool>(m + 1, false));
        dp[0][0] = true;
        for (int i = 1; i < n + 1; ++i){
            auto pp = p[i - 1];
            if(pp == '*') dp[i][0] = dp[i - 2][0];
        }
        for(int i = 1; i < n + 1; ++i)
            for(int j = 1; j < m + 1; ++j){
                auto ss = s[j - 1], pp = p[i - 1];
                if(ss == pp || pp == '.') dp[i][j] = dp[i - 1][j - 1];
                else if(pp == '*'){
                    if(p[i - 2] == ss || p[i - 2] == '.') dp[i][j] = dp[i][j - 1] || dp[i - 2][j];
                    else dp[i][j] = dp[i - 2][j];
                }
            }
        return dp[n][m];
    }
};