class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        int cnt[26] = {};
        for(string &s: B){
            int tmp[26] = {};
            for(char &c: s) ++tmp[c - 'a'];
            for(int i = 0; i < 26; ++i) cnt[i] = max(cnt[i], tmp[i]);
        }
        vector<string> ans;
        for(string &s: A){
            bool flag = true;
            int tmp[26] = {};
            for(char &c: s) ++tmp[c - 'a'];
            for(int i =0; i < 26; ++i) if (tmp[i] < cnt[i]) {flag = false; break;}
            if (flag) ans.push_back(s);
        }
        return ans;
    }
};