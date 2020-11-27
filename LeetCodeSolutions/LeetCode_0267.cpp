class Solution {
public:
    vector<string> generatePalindromes(string s) {
        unordered_map<char, int> cnt;
        for(char &c: s) cnt[c] ++ ;
        int odd = 0;
        char odd_num_char = '\0';
        bool odd_char = false;
        for(auto kv : cnt){
            if (kv.second & 1) {
                ++odd;
                odd_num_char = kv.first;
                odd_char = true;
            }
        }
        if (odd > 1) return {};
        if (odd_char){
            --cnt[odd_num_char];
            if (cnt[odd_num_char] == 0) cnt.erase(odd_num_char);
        }
        for (auto &kv: cnt){
            kv.second /= 2;
        }

        vector<string> ret;
        helper(cnt, ret, 0, s.size() / 2, "");
        // for(auto v: ret){
        //     cout << v << endl;
        // }
        for (auto &v: ret){
            string tmp = v;
            reverse(tmp.begin(), tmp.end());
            if (odd_char) v += odd_num_char;
            v += tmp;
        }
        return ret;
    }

    void helper(unordered_map<char, int> &cnt,
                vector<string> &ret,
                int used,
                int all_num,
                string tmp){
        if (used == all_num){
            ret.push_back(tmp);
            return ;
        }
        for (auto& kv: cnt){
            if(kv.second){
                --kv.second;
                ++used;
                helper(cnt, ret, used, all_num, tmp + kv.first);
                --used;
                ++kv.second;
            }
        }
        return ;
    }
};