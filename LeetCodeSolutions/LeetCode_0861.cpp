class Solution {
public:
    int matrixScore(vector<vector<int>>& A) {
        int row = A.size(), col =A[0].size();
        vector<bool> state(row, false);
        int cnt = 0;
        for (int r = 0; r < row; ++r)
            if (A[r][0] == 0) state[r] = true;

        int ret = 0;
        ret += (1 << (col - 1)) * row;
        for(int c = 1; c < col; ++c)
            ret += helper(A, state, row, col, c);
        return ret;
    }

    int helper(vector<vector<int>> &A, vector<bool> &state, int &row, int &col,int c){
        int cnt = 0;
        for (int r = 0; r < row; ++r){
            if (A[r][c] == 1 && state[r] == false) ++cnt;
            if (A[r][c] == 0 && state[r] == true) ++ cnt;
        }
        if (2 * cnt < row) cnt = row - cnt;
        // cout << "c " << c << " cnt " << cnt << endl;
        return (1 << (col - c - 1)) * cnt;
    }
};