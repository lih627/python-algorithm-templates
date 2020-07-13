class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int> > board{{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
        vector<int> win{2 * 3 * 5, 7 * 11 * 13, 17 * 19 * 23, 2 * 11 * 23,
        5 * 11 * 17, 2 * 7 * 17, 3 * 11 * 19, 5 * 13 * 23};
        int a = 1, b = 1;
        for(int i=0; i < moves.size(); ++i){
            if (i & 1){
                b *= board[moves[i][0]][moves[i][1]];
                for(auto &n: win) if(b % n == 0) return "B";
            }
            else{
                a *= board[moves[i][0]][moves[i][1]];
                for (auto &n: win) if(a % n == 0) return "A";
            }
        }
        if (moves.size() == 9) return "Draw";
        return "Pending";
    }
};