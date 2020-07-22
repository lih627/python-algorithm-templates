#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N皇后
 */

// @lc code=start
class Solution {
public:
    vector<vector<string> > ret;
    vector<vector<string> > solveNQueens(int n) {
        vector<vector<int> > counter(n, vector<int>(n, 0));
        // cout << string(n, '.') << endl;
        vector<string> tmp(n, string(n, '.'));

        helper(tmp, counter, 0, n);
        return ret;
    }

    void helper(vector<string> &tmp, vector<vector<int> > &cnt, int row, int n){
        // for(auto s: tmp){
        //     cout << s << endl;
        // }
        // cout << endl;
        if (row == n) {ret.push_back(tmp);return;}
        for(int i = 0; i < n; ++i){
            if (cnt[row][i] == 0){
                for (int j = 0; j < n; ++j) ++cnt[j][i];
                for (int l = 1; l < n; ++l){
                    int ii = row - l, jj = i - l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    ++cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row + l, jj = i + l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    ++cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row - l, jj = i + l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    ++cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row + l, jj = i - l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    ++cnt[ii][jj];
                }
                tmp[row][i] = 'Q';
                helper(tmp, cnt, row + 1, n);
                tmp[row][i] = '.';
                for (int j = 0; j < n; ++j) --cnt[j][i];
                for (int l = 1; l < n; ++l){
                    int ii = row - l, jj = i - l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    --cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row + l, jj = i + l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    --cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row - l, jj = i + l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    --cnt[ii][jj];
                }
                for (int l = 1; l < n; ++l){
                    int ii = row + l, jj = i - l;
                    if (ii >=n || jj >= n || ii < 0 || jj < 0) break;
                    --cnt[ii][jj];
                }
            }
        }
    }
};
// @lc code=end

