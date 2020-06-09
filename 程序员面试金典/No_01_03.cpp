class Solution {
public:
    string replaceSpaces(string S, int length) {
        string res;
        int cnt = 0;
        for(auto c: S){
            if (cnt == length) break;
            if (c == ' '){res += "%20";}
            else res += c;
            ++cnt;
        }
        return res;
    }
};