class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int odd[n + 2], cnt = 0, res = 0;
        for (int i = 0; i != nums.size(); ++i){
            if (nums[i] &1) odd[++cnt] = i;
        }
        odd[0] = -1; odd[++cnt] = n;
        for(int i = 0; i + k + 1 <= cnt; ++i){
            res += (odd[i + 1] - odd[i]) * (odd[i + k + 1] - odd[i + k]);
        }
        return res;
    }
};