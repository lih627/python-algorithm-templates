#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=164 lang=cpp
 *
 * [164] 最大间距
 */

// @lc code=start
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2) return 0;
        auto [_min, _max] = minmax_element(nums.begin(), nums.end());
        int l = *_min, r = *_max, n = nums.size();
        int bag_size = (r - l) / (n - 1) + 1;
        int num_bag = (r - l  + 1) / bag_size + 1;
        cout << bag_size << ' ' << num_bag << endl;
        vector<int> max_bag(num_bag, INT_MIN), min_bag(num_bag, INT_MAX);
        for (int num: nums){
            int k = (num - l) / bag_size;
            max_bag[k] = max(max_bag[k], num);
            min_bag[k] = min(min_bag[k], num);
        }
        int ret = max_bag[0] - min_bag[0];
        int i = 0;
        while (i < num_bag){
            int j = i + 1;
            while (j < num_bag && min_bag[j] == INT_MAX) ++j;
            if(j < num_bag)ret = max(ret, min_bag[j] - max_bag[i]);
            i = j;
        }
        return ret;
    }
};
// @lc code=end

