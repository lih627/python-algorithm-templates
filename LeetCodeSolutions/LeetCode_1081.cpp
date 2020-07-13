class Solution {
public:
    string smallestSubsequence(string text) {
        unordered_map<char, int> mp;
        for(int i = 0; i < text.size(); ++i){
            mp[text[i]] = i;
        }
        set<char> st;

        vector<char> ret;
        for(int i = 0; i < text.size(); ++i){
            if (st.count(text[i])) continue;
            while(!ret.empty() && text[i] < ret.back()&& mp[ret.back()] > i){
                st.erase(ret.back());
                ret.pop_back();
            }
            ret.push_back(text[i]);
            st.insert(text[i]);
        }
        return {ret.begin(), ret.end()};

    }
};