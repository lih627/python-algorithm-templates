class Solution {
public:
    int maximum69Number (int num) {
        int cnt = 0, k = -1;
        int tmp = num;
        while(tmp){
            if(tmp % 10 == 6){
                k = cnt;
            }
            ++cnt;
            tmp /= 10;
        }
        if (k != -1){
            return num + 3 * pow(10, k);
        }
        return num;
    }
};