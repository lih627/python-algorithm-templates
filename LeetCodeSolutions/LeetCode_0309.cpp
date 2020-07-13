/*
 * @lc app=leetcode.cn id=309 lang=cpp
 *
 * [309] 最佳买卖股票时机含冷冻期
 */

// @lc code=start
#include<vector>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
	int ret=0;
	vector<int> pre{INT_MIN, 0, 0, INT_MIN, 0};
 	for(auto &p: prices){
            vector<int> cur(5, 0);
	        cur[0] = max(pre[2], pre[4]) - p;
	        cur[1] = max(pre[3], pre[0]) + p;
            cur[2] = pre[1];
            cur[3] = max(pre[3], cur[0]);
            cur[4] = max(pre[4], pre[2]);
	        pre = cur;
	}
	for(auto p: pre) ret = max(p, ret);
        return ret;
    }
};
// @lc code=end

