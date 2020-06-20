/*
 * @lc app=leetcode.cn id=408 lang=cpp
 *
 * [408] 有效单词缩写
 */

// @lc code=start
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int w = word.size(), a = abbr.size();
        int i = 0, j = 0;
        while (i < w && j < a){
            if (abbr[j] == '0') return false;
            if (abbr[j] >= '0' && abbr[j] <= '9'){
                int tmp = abbr[j] - '0';
                ++j;
                while(j < a && abbr[j] >='0' && abbr[j] <= '9'){
                    tmp *= 10;
                    tmp += abbr[j] - '0';
                    ++j;
                }
                i += tmp;
            }
            else{
                if (abbr[j] != word[i]) return false;
                ++i;
                ++j;
            }
        }
        return i == w && j == a;
    }
};
// @lc code=end

