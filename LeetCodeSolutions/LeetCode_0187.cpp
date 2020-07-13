/*
 * @lc app=leetcode.cn id=187 lang=cpp
 *
 * [187] 重复的DNA序列
 */

// @lc code=start
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = 10;
        set<string> ret;
        if (s.size() < 10) return {};
        string tmp = s.substr(0, 10);
        set<string> dict;
        dict.insert(tmp);
        for(int i = 10; i < s.size(); ++i){
            tmp.erase(0, 1);
            tmp += s[i];
            if (dict.count(tmp)) ret.insert(tmp);
            else dict.insert(tmp);
        }
        return {ret.begin(), ret.end()};
    }
};
// @lc code=end

