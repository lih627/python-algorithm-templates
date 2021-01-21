int dp[51][51][51];
const int M = 1e9 + 7;
const int DY[] = {-1, 0, 1, 0};
const int DX[] = {0, -1, 0, 1};
typedef long long ll;
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        memset(dp, 0, sizeof(dp));
        if (N == 0) return 0;
        for (int c = 0; c < m; ++c) {
            ++dp[c][0][0];
            ++dp[c][n - 1][0];
        }
        for (int c = 0; c < n; ++c){
            ++dp[0][c][0];
            ++dp[m - 1][c][0];
        }
        int ret = dp[i][j][0];
        for(int c = 1; c < N ; ++c){
            for(int x = 0; x < m; ++x){
                for(int y = 0; y < n; ++y){
                    if (dp[x][y][c - 1]){
                        // dp[x][y][c] += dp[x][y][c - 1];
                        for (int dir = 0; dir < 4; ++dir){
                            int dx = DX[dir], dy = DY[dir];
                            int xx = x + dx, yy = y + dy;
                            if (-1 < xx && xx < m && -1 < yy && yy < n)
                            {
                                dp[xx][yy][c] = (ll(dp[xx][yy][c]) + ll(dp[x][y][c - 1]))%M;
                            }
                        }
                    }
                }
            }
            ret += dp[i][j][c];
            ret %= M;
        }
        return ret;
    }
};