class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        if (s1.length() != s2.length()) return false;
        s1 += s1;
        return s1.find(s2) != -1;
    }
};