class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        vector<int> dp(n, 0);
        if(m == 0 || n == 0) return 0;
        int ret = 0;
        // dp[i][j] = d[i - 1][j - 1] + 1
        // dp[0][j] = 1 if A[0] == B[j]
        for(int j = 0; j < n; ++j)
            if(A[0] == B[j]) {dp[j] = 1; ret = 1;}

        for(int i = 1; i < m; ++i){
            for(int j = n - 1; j > -1; --j){
                if(A[i] == B[j]){
                    dp[j] = j > 0 ? dp[j - 1] + 1: 1;
                    ret = max(dp[j], ret);
                }
                else dp[j] = 0;
            }
        }
        return ret;
    }
};