class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> res(amount+1, 0);
        res[0] = 1;
        for (int coin: coins){
            if (coin ==0) continue;
            for (int i=coin; i<amount+1; ++i){
                res[i] += res[i - coin];
            }
        }
        return res[amount];
    }
};