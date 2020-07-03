class Solution {
public:
    unordered_map<char, int> cnt;

    vector<string> permutation(string S) {
        vector<string> ret;
        int l = 0 ;
        for(auto c: S){
            ++cnt[c];
            ++l;
        }
        helper(ret, {}, 0, l);
        return ret;
    }

    void helper(vector<string> &ret, string tmp, int cur_idx, int l){
        if (cur_idx == l) ret.push_back(tmp);
        else{
            for(auto &n: cnt){
                if (n.second) {
                    --n.second;
                    helper(ret, tmp + n.first, cur_idx + 1, l);
                    ++n.second;
                }
            }
        }
    }

};