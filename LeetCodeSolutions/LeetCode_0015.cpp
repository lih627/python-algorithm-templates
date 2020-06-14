class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> > ret;
        if (nums.size() < 3) return {};
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int l = 0; l < n - 2; ++l){
            if (nums[l] > 0) break;
            if (l > 0 && nums[l] == nums[l - 1]) continue;
            int m = l + 1, r = n - 1;
            while (m < r){
                int s = nums[l] + nums[m] + nums[r];
                if (s < 0){
                    while (m < r && nums[m] == nums[m + 1]) ++m;
                    ++m;
                }
                else if(s > 0){
                    while (r > m && nums[r] == nums[r - 1]) --r;
                    --r;
                }
                else{
                    ret.push_back(vector<int>{nums[l], nums[m], nums[r]});
                    while (m < r && nums[m] == nums[m + 1]) ++m;
                    ++m;
                    while (r > m && nums[r] == nums[r - 1]) --r;
                    --r;
                }
            }
        }
        return ret;
    }
};