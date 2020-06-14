/*
 * @lc app=leetcode.cn id=326 lang=cpp
 *
 * [326] 3的幂
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfThree(int n) {
        return fmod(log10(n) / log10(3),1) == 0;
    }
};
// @lc code=end



/*
 * @lc app=leetcode.cn id=326 lang=cpp
 *
 * [326] 3的幂
 */

// @lc code=start
double EPS = 1e-12;
class Solution {
public:
    int round(double x){
        return x - int(x) >= 0.5? ceil(x): floor(x);
    }
    bool isPowerOfThree(int n) {
        double res = log(n)/log(3);
        return n > 0 && abs(res - round(res)) < EPS;
    }
};
// @lc code=end

