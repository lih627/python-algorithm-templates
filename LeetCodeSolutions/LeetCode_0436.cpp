/*
 * @lc app=leetcode.cn id=436 lang=cpp
 *
 * [436] 寻找右区间
 */

// @lc code=start
#include<vector>
#include<map>

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int, int> mp;
        vector<int> ret;
        for(int i = 0; i < intervals.size(); ++i){
            if (mp.count(intervals[i][0])) continue;
            else mp[intervals[i][0]] = i;
        }
        for (auto &tmp: intervals){
            auto it = mp.lower_bound(tmp[1]);
            if(it == mp.end()) ret.push_back(-1);
            else ret.push_back(it->second);
        }
        return ret;

    }
};
// @lc code=end

