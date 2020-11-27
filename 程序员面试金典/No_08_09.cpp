class Solution {
public:
    vector<string> generateParenthesis(int n) {
        int cnt[2] = {n, n};
        vector<string> ret;
        helper(ret, cnt, "");
        return ret;
    }

    void helper(vector<string> &ret, int cnt[2], string tmp){
        if (cnt[0] == 0 && cnt[1] == 0) ret.push_back(tmp);
        else{
            if(cnt[0] == 0){
                --cnt[1];
                helper(ret, cnt, tmp + ")");
                ++cnt[1];
            }
            else{
                if (cnt[0] < cnt[1]){
                    --cnt[1];
                    helper(ret, cnt, tmp + ")");
                    ++cnt[1];
                }
                --cnt[0];
                helper(ret, cnt, tmp + "(");
                ++cnt[0];

            }
        }
    }
};