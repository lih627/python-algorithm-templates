/*
 * @lc app=leetcode.cn id=276 lang=cpp
 *
 * [276] 栅栏涂色
 */

// @lc code=start
class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0) return n;
        if (n == 1) return k;
        int same = k;
        int diff = k * (k  - 1);
        --n;
        while (--n){
            int tmp = same;
            same = diff;
            diff = (k - 1) * tmp + (k - 1) * diff;
        }
        return diff + same;
    }
};
// @lc code=end

