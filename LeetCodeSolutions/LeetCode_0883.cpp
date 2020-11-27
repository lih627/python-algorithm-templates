class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int ret = 0;
        int xx = grid.size(), yy = grid[0].size();

        for (int i = 0; i < xx; ++i){
            int _tmp = 0;
            for(int j =0; j < yy; ++j){
                if (grid[i][j]) ++ret;
                _tmp = max(_tmp, grid[i][j]);
            }
            ret += _tmp;
        }

        for (int j = 0; j < yy; ++j){
            int _tmp = 0;
            for (int i = 0; i < xx; ++i)
                _tmp = max(_tmp, grid[i][j]);
            ret += _tmp;
        }
        return ret;
    }
};