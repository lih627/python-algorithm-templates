class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        vector<int> ans;
        int i = A.size() - 1, carry = 0;
        while (i > -1 || K || carry){
            int x = i < A.size()? A[i]: 0;
            int y = K % 10;
            int t = x + y + carry;
            ans.push_back(t % 10);
            carry = t / 10;
            K /= 10;
            --i;
        }
        return {ans.rbegin(), ans.rend()};
    }
};