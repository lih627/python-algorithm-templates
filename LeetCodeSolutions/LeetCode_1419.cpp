int flags[100010];
class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        unordered_map<char, int> cnt;
        memset(flags, 0, sizeof(flags));
        int idx = 0;
        for (auto c: croakOfFrogs){
            ++cnt[c];
            if (cnt['c'] >= cnt['r'] && cnt['r'] >= cnt['o']
            && cnt['o'] >= cnt['a'] && cnt['a'] >= cnt['k']){
                if (c == 'c') flags[idx] = 1;
                else if (c == 'k') flags[idx] = -1;
            }
            else return -1;
            ++idx;
        }
        int v = cnt['c'];
        for(auto &p: cnt){
            if (p.second != v) return -1;
        }
        int ret = 0;
        int t = 0;
        for(int i = 0; i < idx; ++i){
            if (flags[i] == 1)
                ++t;
            else if (flags[i] == -1){
                --t;
            }
            ret = max(ret, t);
        }
        return ret;
    }
};