class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        int cnt = 0;
        int maxV = 0;
        for (int i = 0; i < n; ++ i){
            maxV = max(maxV, arr[i]);
            if (i >= maxV) ++cnt;
        }
        return cnt;
    }
};