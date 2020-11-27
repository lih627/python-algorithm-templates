class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int pre = 1, cur = 1;
        for (int i = 0; i < min(n, 10); ++i){
            if (i < 2) cur *= 9;
            else cur *= 10 - i;
            pre += cur;
        }
        return pre;
    }
};