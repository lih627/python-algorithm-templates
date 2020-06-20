/*
 * @lc app=leetcode.cn id=405 lang=cpp
 *
 * [405] 数字转换为十六进制数
 */

// @lc code=start
class Solution {
public:
    string toHex(int num) {
        string ret;
        for(int i = 7; i > -1; --i){
            int cur = ((unsigned)num & (0xf << (i * 4))) >> (i * 4);
            cout << cur << endl;
            if (ret.size() == 0 && cur == 0) continue;
            if (cur < 10) ret += to_string(cur);
            else ret += 'a' + cur - 10;
        }
        return ret.size()? ret: "0";

    }
};
// @lc code=end

