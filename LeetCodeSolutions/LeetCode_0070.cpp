class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) return n;
        int pp = 1, p = 2;
        --n;
        while (--n){
            int cur = pp + p;
            pp = p;
            p = cur;
        }
        return p;
    }
};