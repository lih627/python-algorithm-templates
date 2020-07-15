class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        for(int i = 1; i < n; ++i){
            for(int j = 0; j < i + 1; ++j){
                triangle[i][j] += j != i && j != 0? min(triangle[i - 1][j], triangle[i - 1][j - 1]) : 0;
                triangle[i][j] += j == i? triangle[i - 1][j - 1]: 0;
                triangle[i][j] += j == 0? triangle[i - 1][0]: 0;
            }
        }
        int ret = triangle[n - 1][0];
        for(auto &n: triangle[n - 1]) ret = min(ret, n);
        return ret;
    }
};