#include <vector>
#include <utility>
#include <iostream>
#include <set>
using namespace std;
/*
 * @lc app=leetcode.cn id=327 lang=cpp
 *
 * [327] 区间和的个数
 */

// @lc code=start
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if (nums.size() == 0) return 0;
        multiset<long long> cnt;
        long long prefix = 0;
        cnt.insert(prefix);
        int ret = 0;
        for(auto num: nums){
            prefix += num;
            ret += distance(cnt.lower_bound(prefix - upper), cnt.upper_bound(prefix - lower));
            cnt.insert(prefix);
        }
        return ret;
    }
};
// @lc code=end

