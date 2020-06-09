class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        if (x < 10) return true;
        if (x % 10 == 0) return false;
        int r = 0;
        while (x > r){
            int n = x % 10;
            x /= 10;
            r *= 10;
            r += n;
        }

        return r == x || r / 10 == x;
    }
};