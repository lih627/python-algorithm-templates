class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int p1 = -1, p2 = -1;
        int ans = INT_MAX;
        for(int i = 0; i < words.size(); ++i){
            string &tmp = words[i];
            if (tmp == word1){
                p1 = i;
                if (p2 != -1) ans = min(ans, abs(p1 - p2));
            }
            if (tmp == word2){
                p2 = i;
                if (p1 != -1) ans = min(ans, abs(p1 - p2));
            }
        }
        return ans;
    }
};