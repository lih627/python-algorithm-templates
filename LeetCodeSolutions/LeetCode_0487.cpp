class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ret = 0, cur = 0, pcur = -1;
        for(auto n: nums){
            if(n == 0){
                ret = max(ret, pcur + cur + 1);
                pcur = cur;
                cur = 0;
            }
            else{
                ++cur;
            }
        }
        if(pcur != -1) ret = max(ret, pcur + cur + 1);
        else ret = max(ret, cur);

        return ret;

    }
};