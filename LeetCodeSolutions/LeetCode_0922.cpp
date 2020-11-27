class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> odd;
        for(int i = 0; i < A.size(); i += 2){
            if (A[i]&1) odd.push_back(i);
        }
        int t = 0;
        for (int j = 1; j < A.size(); j += 2){
            if ((A[j] & 1) == 0){
                swap(A[j], A[odd[t]]);
                ++t;
            }
        }
        return A;
    }
};