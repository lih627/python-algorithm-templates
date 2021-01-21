class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r){
            int mid = l + (r - l) / 2;
            if (nums[mid] < target) l = mid + 1;
            else r = mid;
        }
        if (l == nums.size()) return {-1, -1};
        if (nums[l] != target) return {-1, -1};
        int a = 0, b = nums.size();
        while (a < b){
            int m  = a + (b - a) / 2;
            if (nums[m] <= target) a = m + 1;
            else b = m;
        }
        return {l, a - 1};
    }
};