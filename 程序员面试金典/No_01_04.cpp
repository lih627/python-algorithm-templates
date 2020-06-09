class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> counter;
        for (auto c: s) ++counter[c];
        int odd = 0;
        for (auto it: counter){
            if (it.second & 1) ++odd;
            if (odd > 1) return false;
        }
        return true;
    }
};