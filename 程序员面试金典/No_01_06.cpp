class Solution {
public:
    string compressString(string S) {
        int cnt = 0;
        string res;
        for (int i = 0; i < S.size(); ++i){
            if (i == 0) ++cnt;
            if (i > 0){
                if(S[i] == S[i - 1]) ++cnt;
                else{
                    res += S[i - 1] + to_string(cnt);
                    cnt = 1;
                }
            }
            if(i == S.size() - 1) res += S[i] + to_string(cnt);
            }
        return res.size() < S.size()? res: S;
    }
};