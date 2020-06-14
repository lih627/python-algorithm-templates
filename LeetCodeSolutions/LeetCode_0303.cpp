/*
 * @lc app=leetcode.cn id=303 lang=cpp
 *
 * [303] 区域和检索 - 数组不可变
 */

// @lc code=start
class NumArray {
    vector<int> prefix;
public:
    NumArray(vector<int>& nums) {
        for(auto &num: nums){
            if(prefix.empty()) prefix.push_back(num);
            else prefix.push_back(prefix.back() + num);
        }
    }

    int sumRange(int i, int j) {
        if (i) return prefix[j] - prefix[i - 1];
        return prefix[j];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
// @lc code=end

