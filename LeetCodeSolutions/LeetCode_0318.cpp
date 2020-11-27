class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> mask(words.size(), 0);
        for (int i = 0;  i < words.size(); ++i){
            for(char c: words[i]) mask[i] |= 1 << (c - 'a');
        }
        int ret = 0;
        for(int i = 0; i < mask.size(); ++i)
            for(int j = i; j < mask.size(); ++j)
                if((mask[i] & mask[j]) == 0) ret = max(ret, int(words[i].size() * words[j].size()));
        return ret;
    }
};