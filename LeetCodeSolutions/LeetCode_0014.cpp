class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        if (n == 0) return {};
        string ret = strs[0];
        for (int i = 1; i < n; ++i){
            ret = lcs(ret, strs[i]);
        }
        return ret;

    }

    string lcs(string str1, string str2){
        if (str1 == "" || str2  == "") return {};
        string ret;
        for(int i = 0; i < str1.size() && i < str2.size(); ++i){
            if (str1[i] == str2[i]) ret += str1[i];
            else break;
        }
        return ret;
    }
};