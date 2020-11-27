class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        vector<vector<string>> mp(26);
        int ret = 0;
        for (auto s: words){
            reverse(s.begin(), s.end());
            mp[s.back() - 'a'].push_back(s);
        }
        for (char c: S){
            int sz = mp[c - 'a'].size();
            if (sz == 0) continue;
            auto strs = mp[c - 'a'];
            mp[c - 'a'].resize(0);
            for (auto t: strs){
                if (t.size() == 1) {++ret; continue;}
                t.pop_back();
                mp[t.back() - 'a'].push_back(t);
            }
        }
        return ret;
    }
};