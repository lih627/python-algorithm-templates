class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        bool flag = false;
        int _max = nums.size();
        for(auto n: nums){
            if(n == 1) {flag = true; break;}
        }
        if(!flag) return 1;
        for(auto &n :nums){
            if(n > _max || n < 1) n = 1;
        }
        for(auto &n: nums){
            int idx = n < 0? -n - 1: n - 1;
            if(nums[idx] > 0) nums[idx] = -nums[idx];
        }
        int cnt = 1;
        for(auto &n: nums){
            if(n > 0) return cnt;
            ++cnt;
        }
        return cnt;

    }
};