class Solution {
    int memo[1010][1010];
public:
    int longestPalindromeSubseq(string s) {
        memset(memo, -1, sizeof(memo));
        int ans = dp(0, s.size() - 1, s);
        // for(int i = 0; i < s.size(); ++i){
        //     for(int j = i; j < s.size(); ++j){
        //         cout << i << ' ' << j << ' ' << memo[i][j] << endl;
        //     }
        // }
        return ans;
    }

    int dp(int i, int j, string &s){
        if(memo[i][j] != -1) return memo[i][j];
        if(i == j){
            memo[i][j] = 1;
            return memo[i][j];
        }
        if (i + 1 == j){
            if (s[i] == s[j]) memo[i][j] = 2;
            else memo[i][j] = 1;
            return memo[i][j];
        }
        int ret = 0;
        ret = max(ret, dp(i + 1, j, s));
        ret = max(ret, dp(i, j -1, s));
        ret = max(ret , dp(i + 1, j - 1, s) + 2 * (s[i] == s[j]));
        memo[i][j] = ret;
        return memo[i][j];
    }
};