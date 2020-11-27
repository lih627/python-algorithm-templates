const int MOD = pow(10, 9) + 7;

class Solution {
public:
    int numWays(int steps, int arrLen) {
        arrLen = min(arrLen, steps);
        vector<int> dp(arrLen, 0), tmp(arrLen, 0);
        for(int i = 0; i < steps; ++i){
            if (i == 0){
                dp[0] = 1;
                dp[1] = 1;
                continue;
            }
            for(int k = 0; k < dp.size(); ++k){
                int a = k > 0? dp[k - 1]: 0;
                int b = dp[k];
                int c = k + 1 < dp.size()? dp[k + 1]: 0;
                tmp[k] = a + b;
                tmp[k] %= MOD;
                tmp[k] += c;
                tmp[k] %= MOD;
            }
            swap(dp, tmp);
            tmp.assign(tmp.size(), 0);
        }
        return dp[0];
    }
};