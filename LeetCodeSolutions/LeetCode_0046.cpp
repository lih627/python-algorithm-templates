class Solution {
public:
    void backtrack(int idx, vector<int> &nums, vector<vector<int>> &res, vector<int> &tmp, vector<bool> &used){
        if (idx == used.size()){
            res.push_back(tmp);
            return ;
        }
        for (int i=0; i!=used.size(); ++i){
            if (!used[i]){
                used[i] = true;
                tmp.push_back(nums[i]);
                backtrack(idx + 1, nums, res, tmp, used);
                used[i] = false;
                tmp.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.empty()) return res;
        int sz = nums.size();
        vector<int> tmp = {};
        vector<bool> used(sz, false);
        backtrack(0, nums, res, tmp, used);
        return res;
    }
};