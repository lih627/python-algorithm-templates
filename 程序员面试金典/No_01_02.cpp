class Solution {
public:
    bool CheckPermutation(string s1, string s2) {
        unordered_map<char, int> dict;
        if (s1.size() != s2.size()) return false;
        for (auto c: s1){
            dict[c] += 1;
        }
        for (auto c: s2){
            if (dict[c]) dict[c] -= 1;
            else return false;
        }
        return true;
    }
};