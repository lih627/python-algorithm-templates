class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int l = 0, r = 0, total = 0;
        int ans  = INT_MAX;
        while(r < nums.size()){
            while (r < nums.size() && total < s){
                total += nums[r];
                ++r;
            }
            while(l < r && total - nums[l] >= s){
                total -= nums[l];
                ++l;
            }
            if(total >= s) ans = min(ans, r - l);
            total -= nums[l];
            ++l;
        }
        return ans == INT_MAX? 0: ans;
    }
};