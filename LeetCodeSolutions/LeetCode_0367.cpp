class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 0) return false;
        int l = 0, r = num;
        while (l <= r){
            long int mid = l + (r - l >> 1);
            if (mid * mid < num) l = mid + 1;
            else if (mid * mid > num) r = mid - 1;
            else return true;
        }
        return false;

    }
};