/*
 * @lc app=leetcode.cn id=293 lang=cpp
 *
 * [293] 翻转游戏
 */

// @lc code=start
class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        unordered_set<int> pos;
        vector<string> ret;
        for(int i = 0; i < s.size(); ++i) if(s[i] =='
        +') pos.insert(i);
        for (auto it: pos){
            if (pos.count(it + 1)) ret.push_back(s.substr(0, it) + "--" + s.substr(it + 2, s.size() - 1));
        }
        return ret;
    }
};
// @lc code=end

