class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        vector<int> idegree(N, 0), odegree(N, 0);
        for(auto a: trust){
            int i = a[0] - 1, j = a[1] - 1;
            ++odegree[i];
            ++idegree[j];
        }
        for(int i = 0; i < N; ++i){
            if (idegree[i] == N - 1 && odegree[i] == 0) return i + 1;
        }
        return -1;
    }
};