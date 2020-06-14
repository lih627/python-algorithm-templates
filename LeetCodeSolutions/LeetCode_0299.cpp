/*
 * @lc app=leetcode.cn id=299 lang=cpp
 *
 * [299] 猜数字游戏
 */

// @lc code=start
class Solution {
public:
    string getHint(string secret, string guess) {
        int cntA = 0;
        unordered_map<char, int> cs, cg;
        for (int i = 0 ; i < secret.size(); ++i){
            if (secret[i] == guess[i]) ++cntA;
            else{++cs[secret[i]], ++cg[guess[i]];}
        }
        int cntB = 0;
        for(auto pc: cs){
            if (cg.count(pc.first)) cntB += min(pc.second, cg[pc.first]);
        }
        return to_string(cntA) + "A" + to_string(cntB) + "B";

    }
};
// @lc code=end

