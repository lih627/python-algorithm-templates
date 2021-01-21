class Solution {
public:
    int numSub(string s) {
        int ret = 0, pre = 0;
        const int M = 1e9 + 7;
        for(auto &c: s){
            if (c == '0') pre = 0;
            else{
                int cur = pre + 1;
                cur %= M;
                pre = cur;
                ret = (ret + cur) % M;
            }
        }
        return ret;
    }
};