class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ret = nums[0] + nums[1] + nums[2];
        int delta = abs(target - ret);
        for(int l = 0; l < n - 2; ++l){
            int m = l + 1, r = n - 1;
            if(l > 0 && nums[l - 1] == nums[l]) continue;
            if (delta == 0) break;
            while (m < r){
                int cur = nums[l] + nums[m] + nums[r];
                int cd = cur - target;
                int acd = abs(cd);
                if (acd < delta){
                    ret = cur;
                    delta = acd;
                }
                if (cd == 0){
                    ret = cur;
                    break;
                }
                else if(cd < 0){
                    while(m + 1 < r && nums[m] == nums[m + 1]) ++m;
                    ++m;
                }
                else if(cd > 0){
                    while (r - 1 > m && nums[r] == nums[r - 1]) --r;
                    --r;
                }

            }
        }
        return ret;
    }
};