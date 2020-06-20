class Solution {
public:
    bool isPalindrome(string s) {
        string ss;
        for(auto c: s){
            if ((c >= 'a' && c <= 'z')||(c >= 'A' && c <= 'Z')||(c >='0' && c<='9')) ss += c;
        }
        int i = 0, j = ss.size() - 1;
        while (i < j){
            auto a = ss[i], b = ss[j];
            if (a >= 'A' && a <= 'Z') a = 'a' + a - 'A';
            if (b >= 'A' && b <= 'Z') b = 'a' + b - 'A';
            if (a != b) return false;
            ++i;
            --j;
        }
        return true;
    }
};