class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.size()) return "0";
        int i = 0, cnt = 0, sz = num.size();
        vector<char> ret;
        while (i < sz && cnt < sz - k){
            int select_id = i;
            char select_char = num[i];
            int j = i + 1;
            while(j < k + cnt + 1){
                if(select_char > num[j]){
                    select_char = num[j];
                    select_id = j;
                }
                ++j;
            }
            ++cnt;
            // cout << select_char << endl;
            ret.push_back(select_char);
            i = select_id + 1;
        }
        int s = 0;
        while (s < ret.size() && ret[s] =='0') ++s;
        string ans;
        if (s == ret.size()) return "0";
        while(s < ret.size()){
            cout << ret[s];
            ans += ret[s];
            ++s;
        }
        return ans;
    }
};