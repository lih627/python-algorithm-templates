class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.empty()) return;
        int row = matrix.size(), col = matrix[0].size();
        for(int r = 0; r < row / 2; ++r){
            for(int c = 0; c < col; ++c) swap(matrix[r][c], matrix[row -  r - 1][c]);
        }
        for (int r = 0; r < row; ++r)
            for(int c = r + 1; c < col; ++c){
                swap(matrix[r][c], matrix[c][r]);
            }
        return;
    }
};