class Solution {
    int cnt[26];
public:
    bool buddyStrings(string A, string B) {
        if (A.size() != B.size()) return false;
        memset(cnt, 0, sizeof(cnt));
        bool twice = false;
        vector<int> indexs;
        for (int i = 0; i < A.size(); ++i){
            if (A[i] != B[i]){
                indexs.push_back(i);
            }
            ++cnt[A[i] - 'a'];
            if (cnt[A[i] - 'a'] > 1) twice = true;
        }
        // for (auto c: indexs) cout << c << ' ';
        if (indexs.empty()) return twice;
        if (indexs.size() != 2) return false;
        return (A[indexs[0]] == B[indexs[1]]) && (A[indexs[1]] == B[indexs[0]]);
    }
};