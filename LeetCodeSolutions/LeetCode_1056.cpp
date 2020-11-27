const int dict[] ={0, 1, -1, -1, -1, -1, 9, -1, 8, 6};
class Solution {
public:
    bool confusingNumber(int N) {
        int tmp = N, ret = 0;
        while(tmp){
            if (dict[tmp % 10] == -1){
                return false;
            }
            ret  *= 10;
            ret += dict[tmp % 10];
            tmp /= 10;
        }
        return ret != N;
    }
};l