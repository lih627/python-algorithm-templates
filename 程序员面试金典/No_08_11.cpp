class Solution {
private:
    static constexpr int mod = 1000000007;
    static constexpr int coins[4] = {25, 10, 5, 1};

public:
    int waysToChange(int n) {
        vector<int> res(n + 1, 0);
        res[0] = 1;

        for (int coin: coins){
            for (int i = coin; i < n + 1; ++i){
                res[i] += res[i - coin];
                res[i] %= mod;
            }
        }
        return *(res.end() - 1);
    }
};

const int MOD = 1000000007;
class Solution {
public:
    int waysToChange(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        vector<int> coins{1, 5, 10, 25};
        for (auto coin: coins)
            for (int i = 0; i + coin < n + 1; ++i){
                dp[i + coin] += dp[i];
                dp[i + coin] %= MOD;
            }
        return dp[n];
    }
};