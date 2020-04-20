class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        decltype(nums.size()) l = 0, r = nums.size();
        while (l < r){
            auto mid = l + (r - l) / 2;
            if (mid == nums.size() - 1 || nums[mid] > nums[mid + 1]){
                r = mid;
            }
            else{
                l = mid + 1;
            }
        }
        return l;
    }
};