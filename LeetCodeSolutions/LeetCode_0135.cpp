#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=135 lang=cpp
 *
 * [135] 分发糖果
 */

// @lc code=start
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> tmp(n, 1);
        for (int i = n - 2; i > -1; --i){
            if (ratings[i] > ratings[i + 1]) tmp[i] = tmp[i + 1] + 1;
        }
        int ret = 0;
        int pre = 1;
        for (int i = 0; i < n; ++i){
            if (i == 0){
                ret += max(pre, tmp[i]);
            }
            else if (ratings[i] > ratings[i  - 1]){
                pre += 1;
                ret += max(pre, tmp[i]);
            }
            else {pre = 1; ret+= max(pre, tmp[i]);};
        }
        return ret;
    }
};
// @lc code=end

