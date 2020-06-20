/*
 * @lc app=leetcode.cn id=434 lang=cpp
 *
 * [434] 字符串中的单词数
 */

// @lc code=start
class Solution {
public:
    int countSegments(string s) {
        int j = 0;
        int cnt = 0;
        while (j < s.size()){
            if (s[j] == ' ') ++j;
            else{
                ++cnt;
                while(j < s.size() && s[j] != ' ') ++j;
            }
        }
        return cnt;
    }
};
// @lc code=end

