class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int row = M.size();
        if(row == 0) return {};
        int col = M[0].size();
        vector<vector<int> > ret(row, vector<int>(col, 0));
        for(int x = 0; x < row; ++x)
            for(int y = 0; y < col; ++y){
                int cnt = 0;
                for(int dx = -1; dx < 2; ++dx)
                    for(int dy = -1; dy < 2; ++dy)
                    {
                        int cx = x + dx, cy = y + dy;
                        if(cx > -1 && cx < row && cy >-1 && cy < col){
                            ++cnt;
                            ret[x][y] += M[cx][cy];
                        }
                    }
                ret[x][y] /= cnt;
            }
        return ret;
    }
};