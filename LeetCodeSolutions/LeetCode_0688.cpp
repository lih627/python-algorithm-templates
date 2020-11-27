const int DX[] = {-2, -1, 1, 2, 2, 1, -1, -2};
const int DY[] = {1, 2, 2, 1, -1, -2, -2, -1};
class Solution {
public:
    double knightProbability(int N, int K, int r, int c) {
        double dp[N][N][K + 1];
        memset(dp, 0, sizeof(dp));
        for(int k = 0; k <= K; ++k){
            if (k == 0) dp[r][c][k] = 1;
            else{
                for(int x = 0; x < N; ++x){
                    for(int y = 0; y < N; ++y){
                        if (dp[x][y][k - 1] > 0){
                            for(int z = 0; z < 8; ++z){
                                int xx = DX[z] + x, yy = DY[z] + y;
                                if (-1 < xx && xx < N && -1 < yy && yy < N)
                                    dp[xx][yy][k] += dp[x][y][k - 1] / 8.0;
                            }
                        }
                    }
                }
            }
        }
        double ret = 0;
        for (int i = 0; i < N; ++i)
            for(int j = 0; j < N; ++j)
                ret += dp[i][j][K];
        return ret;
    }
};