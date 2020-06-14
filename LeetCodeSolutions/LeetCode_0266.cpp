/*
 * @lc app=leetcode.cn id=266 lang=cpp
 *
 * [266] 回文排列
 */

// @lc code=start
class Solution {
public:
    bool canPermutePalindrome(string s) {
        vector<int> cnt(256, 0);
        for (auto c: s) ++cnt[c];
        int odd = 0;
        for(auto i: cnt)
            if(i & 1) ++odd;
        return odd <= 1;
    }
};
// @lc code=end

