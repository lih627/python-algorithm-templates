class Solution {
    unordered_set<char> st;
public:
    bool isUnique(string astr) {
        for (auto c: astr){
            if (st.count(c)) return false;
            st.insert(c);
        }
        return true;
    }
};