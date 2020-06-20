/*
 * @lc app=leetcode.cn id=414 lang=cpp
 *
 * [414] 第三大的数
 */

// @lc code=start
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int MIN = 1 << 31;
        vector<long long int> ans;
        // cout << MIN << endl;
        for (auto n: nums){
            if (ans.empty()) ans.push_back(n);
            else if (ans.size() < 3){
                bool add = false;
                for(int i = 0; i < ans.size(); ++i){
                    if(n == ans[i]) {add = true;break;}
                    if(n > ans[i]){
                        ans.push_back(ans.back());
                        for(int j = ans.size() - 1; j > i; --j){
                            ans[j] = ans[j - 1];
                        }
                        ans[i] = n;
                        add = true;
                        break;
                    }
                }
                if (!add) ans.push_back(n);
            }
            else{
                for (int i = 0; i < ans.size(); ++i){
                    if (n == ans[i]) break;
                    if(n > ans[i]){
                        for(int j = ans.size() - 1; j > i; --j){
                            ans[j] = ans[j - 1];
                        }
                        ans[i] = n;
                        break;
                    }
                }
            }
        }
        if (ans.empty()) return 0;
        if(ans.size() < 3) return ans[0];
        return ans[2];
    }
};
// @lc code=end

