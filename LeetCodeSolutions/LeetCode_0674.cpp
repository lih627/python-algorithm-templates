class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int ret = 0;
        int l = 0, r = 0;
        while(r < nums.size()){
            if(r > 0 && nums[r] <= nums[r - 1]) l = r;
            ret = max(r - l + 1, ret);
            ++r;
        }
        return ret;

    }
};