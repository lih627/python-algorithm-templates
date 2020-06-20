/*
 * @lc app=leetcode.cn id=422 lang=cpp
 *
 * [422] 有效的单词方块
 */

// @lc code=start
class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        if (words.empty()) return true;
        if(words[0].size() != words.size()) return false;
        for(int i = 0; i < words.size(); ++i){
            string tmp;
            for (int j = 0; j < words.size(); ++j){
                if (i < words[j].size()) tmp += words[j][i];
                else break;
            }
            if (tmp != words[i]) return false;
        }
        return true;
    }
};
// @lc code=end

