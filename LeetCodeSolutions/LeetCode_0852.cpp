class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int ret = 0;
        for(int idx = 0; idx != A.size(); ++idx){
            if (idx == 0 || idx == A.size() - 1) continue;
            if (A[idx] > A[idx - 1] && A[idx] > A[idx + 1]){
                ret = idx;
                break;
            }
        }
        return ret;
    }
};