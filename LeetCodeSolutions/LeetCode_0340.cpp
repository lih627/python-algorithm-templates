class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int> counter;
        int ret = 0;
        int tmp = 0;
        for(int i = 0; i < s.size(); ++i){
            char &c = s[i];
            ++counter[c];
            ++tmp;
            if(counter.size() <= k){
                ret = max(ret, tmp);
            }
            if(counter.size() == k + 1){
                int st = i - tmp + 1;
                while(counter.size() > k){
                    char key = s[st];
                    --counter[key];
                    --tmp;
                    if(counter[key] == 0){
                        counter.erase(counter.find(key));
                    }
                    ++st;
                }
            }
        }
        return ret;
    }
};