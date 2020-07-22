class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int> > vec;
        int cur_cnt = 0;
        for (int i = 0; i < s.size(); ++i){
            if(vec.empty() || s[i] != vec.back().first){
                vec.push_back(make_pair(s[i], 1));
            }
            else{
                if(s[i] == vec.back().first){
                    ++vec.back().second;
                }
            }
            if(vec.back().second == k) vec.pop_back();
        }
        string ret;
        for (auto p: vec){
            int i = 0;
            while(i < p.second) { ++i; ret += p.first;}
        }
        return ret;
    }
};