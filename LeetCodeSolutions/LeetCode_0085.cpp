class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> m(row, vector<int>(col, 0));
        int ret = 0;
        for(int r = 0; r < row; ++r)
            for(int c = 0; c < col; ++c){
                if (matrix[r][c] == '0') continue;
                m[r][c] = r > 0? 1 + m[r - 1][c]: 1;
            }

        for(int r = 0; r < row; ++r){
            vector<int> stk;
            vector<int> right(col, 0);
            for(int c = col - 1; c >= 0; --c){
                while(!stk.empty() && m[r][stk.back()] >= m[r][c]) stk.pop_back();
                right[c] = stk.empty()? col: stk.back();
                stk.push_back(c);
            }
            stk.resize(0);
            for(int c = 0; c < col; ++c){
                while(!stk.empty() && m[r][stk.back()] >= m[r][c]) stk.pop_back();
                int l = -1;
                if (!stk.empty()) l = stk.back();
                stk.push_back(c);
                ret = max(ret, (right[c] - l - 1) * m[r][c]);
            }
        }
        return ret;
    }
};