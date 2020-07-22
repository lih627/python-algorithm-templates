class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        if (r == 0) return 0;
        while (l < r){
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) r = mid;
            else  l = mid + 1;
        }
        return l;
    }
};