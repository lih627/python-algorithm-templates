class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int ans = 0, l = 0, r = nums.size() - 1;
        for (int i = 0; i < nums.size(); ++i){
            int c = target - nums[i];
            int l = i + 1, r = nums.size() - 1;
            while (l < r){
                if (nums[l] + nums[r] < c){
                    ans += r - l;
                    l += 1;
                }
                else r -= 1;
            }
        }
        return ans;
    }
};