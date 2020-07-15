class Solution {
public:
    unordered_map<int, int> memo;
    int numTrees(int n) {
        return dp(n);
    }

    int dp(int n){
        if (n == 1 || n == 0)  memo[n] = 1;
        if(memo.count(n)) return memo[n];
        int ret = 0;
        for(int i = 1; i < n + 1; ++i){
            int l = i - 1;
            int r = n - i;
            ret += dp(l) * dp(r);
        }
        memo[n] = ret;
        return memo[n];
    }

};