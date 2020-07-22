class Solution {
public:
    map<vector<int>, bool> dp;
    bool isInterleave(string s1, string s2, string s3) {
        dp.clear();
        int i = s3.size(), j = s1.size(), k = s2.size();
        return helper({i, j, k}, s1, s2, s3);
    }

    bool helper(vector<int> state, string &s1, string &s2, string &s3){
        int i = state[0], j = state[1], k = state[2];
        if (dp.count(state)) return dp[state];
        if(i != j + k) {
            dp[state] = false;
            return false;
        }
        if (j > s1.size() || k > s2.size()){
            dp[state] = false;
            return dp[state];
        }
        // i: s3, j: s1, k:s2
        if (i == 0 && j == 0 && k==0){
            dp[state] = true;
            return dp[state];
        }
        if (i > 0 && j > 0 && s3[i - 1] == s1[j - 1] && helper({i - 1, j - 1, k}, s1, s2, s3)){
            dp[state] = true;
            return dp[state];
        }
        if (i > 0 && k > 0 && s3[i - 1] == s2[k -1] && helper({i - 1, j, k - 1}, s1, s2, s3)){
            dp[state] = true;
            return dp[state];
        }
        dp[state] = false;
        return dp[state];
    }

};