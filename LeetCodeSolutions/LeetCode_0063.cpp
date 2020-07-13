/*
 * @lc app=leetcode.cn id=63 lang=cpp
 *
 * [63] 不同路径 II
 */

// @lc code=start
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        if (row == 0) return 0;
        int col = obstacleGrid[0].size();
        vector<int> dp(col, 0);
        dp[0] = obstacleGrid[0][0] ? 0: 1;
        for (int i = 0; i < row; ++i)
            for(int j = 0 ; j < col; ++j){
                if(obstacleGrid[i][j]) {dp[j] = 0; continue;}
                dp[j] += j > 0 ? dp[j - 1] : 0;
            }
        return dp[col - 1];
    }
};
// @lc code=end

