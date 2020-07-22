class Solution {
public:
    int memo[510][510];

    int maxCoins(vector<int>& nums) {
        memset(memo, 0, sizeof(memo));
        return dp(0, nums.size() - 1, nums);
    }

    int dp(int i, int j, vector<int> &nums){
        if (j < i || i < 0 || j < 0 || i > nums.size() - 1 || j > nums.size() - 1){
            return 0;
        }
        if (memo[i][j]) return memo[i][j];
        if (i == j){
            int ret = 1;
            int l = i - 1 >= 0? nums[i - 1]: 1;
            int r = i + 1 < nums.size()? nums[i + 1]: 1;
            memo[i][j] = l * nums[i] * r;
            return memo[i][j];
        }
        int ret= 0;
        int l = i - 1 >= 0? nums[i - 1]: 1;
        int r = j + 1 < nums.size()? nums[j + 1]: 1;
        for (int k = i; k <= j; ++k){
            ret = max(ret, dp(i, k - 1, nums) + dp(k + 1, j, nums) + l * r * nums[k]);
        }
        memo[i][j] = ret;
        return ret;
    }

};
