class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char> trans{{'1', '1'}, {'6', '9'}, {'8', '8'}, {'0', '0'}, {'9', '6'}};
        int l = 0, r = num.size() - 1;
        if (r < 0) return false;
        while (l <= r){
            if (trans[num[l]] != num[r]) return false;
            ++l;
            --r;
        }
        return true;
    }
};