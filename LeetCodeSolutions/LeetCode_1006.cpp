class Solution {
public:
    int clumsy(int N) {
        long long prev = N;
        --N;
        if(N > 0)
            prev *= N;
        --N;
        if (N > 0)
            prev /= N;
        --N;
        while (N > 0){
            prev += N;
            --N;
            int tmp = N;
            --N;
            if (N > 0){
                tmp *= N;
                --N;
            }
            if (N > 0){
                tmp /= N;
                --N;
            }
            prev -= tmp;
        }
        return prev;
    }
};