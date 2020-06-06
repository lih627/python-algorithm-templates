class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for (auto &num: nums) st.insert(num);

        int res = 0;
        int cur = 0;
        for (auto num: st){
            if (st.count(num - 1) == 0){
                cur = 1;
            while (st.count(num + 1)){
                ++cur;
                ++num;
            }
            }
            res = max(res, cur);
        }
        return res;
    }
};