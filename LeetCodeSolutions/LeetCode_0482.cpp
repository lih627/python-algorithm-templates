class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        string ret;
        int cnt = 0;
        for(auto it = S.rbegin(); it != S.rend(); ++it){
            if(isalnum(*it)) {
                if(cnt == K){ret += '-'; cnt = 0;}
                ret += toupper(*it);
                ++cnt;
            }
        }
        return {ret.rbegin(), ret.rend()};
    }
};