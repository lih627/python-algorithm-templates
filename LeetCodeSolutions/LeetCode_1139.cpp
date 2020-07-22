#include <iostream>
#include <vector>

using namespace std;
/*
 * @lc app=leetcode.cn id=1139 lang=cpp
 *
 * [1139] 最大的以 1 为边界的正方形
 */

// @lc code=start
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int> >& grid) {
        if (grid.size() == 0) return 0;
        int row = grid.size(), col = grid[0].size();
        int ret = 0;
        vector<vector<int> > up(row, vector<int>(col, 0)), left(row, vector<int>(col, 0));
        for(int i = 0; i < row; ++i){
            for (int j = 0; j < col; ++j){
                if (grid[i][j] > 0){
                    ret = 1;
                    left[i][j] = j > 0 ? grid[i][j] + left[i][j - 1]: grid[i][j];
                    up[i][j] = i > 0 ? grid[i][j] + up[i - 1][j] : grid[i][j];
                }
            }
        }

        if(ret == 0) return ret;

        for(int i = 0; i < row; ++i){
            for(int j = 0; j < col; ++j){
                int cur_max = min(left[i][j], up[i][j]);
                if (cur_max <= ret) continue;
                for(int len = ret + 1; len <= cur_max; ++len){
                    int ll = left[i - len + 1][j];
                    int uu = up[i][j - len + 1];
                    if (min(ll, uu) >= len){
                        ret = max(ret, len);
                    }
                }

            }
        }
        return ret * ret;

    }
};
// @lc code=end

