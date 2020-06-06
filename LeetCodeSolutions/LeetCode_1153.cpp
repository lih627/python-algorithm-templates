class Solution {
public:
    bool canConvert(string str1, string str2) {
        if(str1 == str2) return true;
        vector<int> s2(26, 0);
        int cnt = 0;
        for(auto s: str2){
            if (s2[s - 'a'] == 0){
                ++cnt;
            }
            ++s2[s - 'a'];
        }
        if (cnt == 26) return false;
        vector <int> mp(26, -1);
        for(int i=0; i < str1.length(); ++i){
            if (mp[str1[i]- 'a'] == -1){
                mp[str1[i] - 'a'] = str2[i] - 'a';
            }
            else{
                if (str2[i] - 'a' != mp[str1[i] - 'a']) return false;
            }
        }
        return true;
    }
};