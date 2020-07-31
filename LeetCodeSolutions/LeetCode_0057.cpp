#include<iostream>
#include<vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=57 lang=cpp
 *
 * [57] 插入区间
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        intervals.push_back(newInterval);
        sort(intervals.begin(), intervals.end());
        vector<vector<int> > ret;
        vector<int> tmp = intervals[0];
        for (auto interval: intervals){
            if (interval[0] >= tmp[0] && interval[0] <= tmp[1]) tmp[1] = max(tmp[1], interval[1]);
            else{
                ret.push_back(tmp);
                tmp = interval;
            }
        }
        ret.push_back(tmp);
        return ret;
    }
};
// @lc code=end

