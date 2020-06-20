class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int n = A.size(), pmax = A[0];
        int ans = 0;
        for (int i = 1; i < n; ++i){
            ans = max(pmax + A[i] - i, ans);
            pmax = max(pmax, A[i] + i);
        }
        return ans;
    }
};