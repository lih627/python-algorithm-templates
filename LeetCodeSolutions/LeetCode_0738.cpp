int isvalid(vector<int>  & t){
    int i = 1;
    for(; i < t.size(); ++i){
        if (t[i] < t[i - 1]) break;
    }
    return i;
}

class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string s = to_string(N);
        int n = s.size();
        vector<int> tmp;
        for(auto c: s) tmp.push_back(c - '0');
        // for(auto c: tmp) cout << c << endl;
        int t = isvalid(tmp);
        while (t < n){
            for(int j = t; j < n; ++j){
                tmp[j] = 9;
            }
            --tmp[t - 1];
            t = isvalid(tmp);
        }
        int ret = 0;
        for(auto m: tmp){
            ret *= 10;
            ret += m;
        }
        return ret;
    }
};