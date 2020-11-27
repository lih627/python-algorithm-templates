class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       int insert_idx = 0, cur = 0;
       while(cur < nums.size()){
           if (nums[cur]){
               nums[insert_idx] = nums[cur];
               ++insert_idx;
           }
           ++cur;
       }
       for (; insert_idx < nums.size(); ++insert_idx)
            nums[insert_idx] = 0;
    }
};