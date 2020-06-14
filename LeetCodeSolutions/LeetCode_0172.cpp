class Solution {
public:
    int titleToNumber(string s) {
        int ret = 0;
        for (auto c: s){
            ret *= 26;
            ret += (int)(c - 'A' + 1);
        }
        return ret;
    }
};