class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int row = board.size();
        if (row == 0) return ;
        int col = board[0].size();
        for(int i = 0; i < row; ++i)
            for(int j = 0; j < col; ++j)
                trans(board, i, j, row, col);
        for(int i = 0; i < row; ++ i)
            for(int j = 0; j < col; ++j)
                board[i][j] >>= 1;

    }

    void trans(vector<vector<int> >&board, int i, int j, int& row, int& col){
        int cnt = 0;
        for(int di = -1; di < 2; ++di)
            for(int dj = -1; dj < 2; ++ dj)
            {
                if(di == 0 && dj == 0) continue;
                int  ci = i + di, cj = j + dj;
                if(ci < 0  || ci >= row) continue;
                if(cj < 0 || cj >= col) continue;
                cnt += board[ci][cj] & 1;
            }
        if(board[i][j]){
            if(cnt == 2 || cnt == 3) board[i][j] = (1 << 1) + board[i][j];
        }
        else{
            if(cnt == 3) board[i][j] = 1 << 1;
        }
    }


};