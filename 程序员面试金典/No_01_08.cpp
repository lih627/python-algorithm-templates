class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> row, col;
        int m = matrix.size();
        if (m == 0) return;
        int n = matrix[0].size();
        for(int i = 0; i < m; ++i)
            for(int j = 0; j < n; ++j){
                if (!matrix[i][j]){
                    row.insert(i);
                    col.insert(j);
                }
            }
        for(int i = 0; i < m; ++i)
            for(int j = 0; j < n; ++j){
                if (row.count(i) || col.count(j)){
                    matrix[i][j] = 0;
                }
            }
    }
};