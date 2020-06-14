/*
 * @lc app=leetcode.cn id=256 lang=cpp
 *
 * [256] 粉刷房子
 */

// @lc code=start
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        vector<int> pre(3, 0), cur(3, 0);
        for(int i = 0; i < costs.size(); ++i){
            if(i == 0) pre = costs[i];
            else{
                cur[0] = min(pre[1], pre[2]) + costs[i][0];
                cur[1] = min(pre[0], pre[2]) + costs[i][1];
                cur[2] = min(pre[0], pre[1]) + costs[i][2];
                pre = cur;
            }
        }
        return *min_element(pre.begin(), pre.end());
    }
};
// @lc code=end
