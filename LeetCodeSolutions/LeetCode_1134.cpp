class Solution {
public:
    bool isArmstrong(int N) {
        int t = N, k = 0, ret = 0;
        while (t){
            ++k;
            t /= 10;
        }
        t = N;
        while(t){
            int c = t % 10;
            ret += pow(c, k);
            t /= 10;
        }
        return ret == N;
    }
};