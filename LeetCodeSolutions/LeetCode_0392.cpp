/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */

// @lc code=start
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.size(), n = t.size(), i = 0, j = 0;

        while (j < n){
        if(t[j] == s[i]){++j; ++i;}
        else ++j;
        if (i == m) return true;
        }
        return j == n && i == m;
    }
};
// @lc code=end

