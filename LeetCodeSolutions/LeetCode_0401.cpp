/*
 * @lc app=leetcode.cn id=401 lang=cpp
 *
 * [401] 二进制手表
 */

// @lc code=start
class Solution {
    unordered_map<int, vector<int> > mp;
public:
    vector<string> readBinaryWatch(int num) {
        vector<bool> used(6, false);
        for (int i = 0; i < 6; ++i){
            helper(0, used, -1, 0, i);
        }
        // for (auto k: mp){
        //     for (auto num: k.second)
        //         cout << k.first << num << endl;
        // }
        vector<string> ret;
        for (int h = 0; h <= num; ++h){
            for (auto hour: mp[h]){
                string ans;
                if(hour < 12){
                    ans = to_string(hour);
                    ans += ":";
                    for (auto mins: mp[num - h]){
                        if (mins < 10){
                            ret.push_back(ans + "0" + to_string(mins));
                        }
                        else if(mins < 60){
                            ret.push_back(ans + to_string(mins));
                        }

                    }
                }
            }
        }
        return ret;

    }
    void helper(int cur, vector<bool> &used, int lb, int tmp, int num){
        if (cur == num){
            mp[num].push_back(tmp);
            return;
        }
        for (int i = lb + 1; i < used.size(); ++i){
            if (!used[i]){
                used[i] = true;
                helper(cur + 1, used, i,tmp + (1 << i), num);
                used[i] = false;
            }
        }
    }
};
// @lc code=end

