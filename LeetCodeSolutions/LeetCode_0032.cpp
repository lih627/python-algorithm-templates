class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        stk.push(-1);
        int ret = 0;
        for(int i = 0; i < s.size(); ++i){
            if (s[i] == '(') stk.push(i);
            else{
                stk.pop();
                if(stk.empty()) stk.push(i);
                else ret = max(ret, i - stk.top());
            }
        }
        return ret;
    }
};


class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        vector<int> dp(n, 0);
        int ret = 0;
        for(int i = 0; i < n; ++i){
            if (s[i] == ')'){
                if (i > 0 && s[i - 1] == '('){
                    if(i > 1) dp[i] = dp[i - 2] + 2;
                    else dp[i] = 2;
                }
                else{
                    if(i > 1 && dp[i - 1] > 0){
                        int tmp = i - dp[i - 1] - 1;
                        if (tmp < 0) continue;
                        if (tmp == 0 && s[0] == '(') dp[i] = dp[i - 1] + 2;
                        if(tmp > 0  && s[tmp] == '(') dp[i] = 2 + dp[i - 1] + dp[tmp - 1];
                    }
                }
            }
            ret = max(ret, dp[i]);
        }
        return ret;
    }
};