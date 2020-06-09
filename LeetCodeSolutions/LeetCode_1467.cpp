class Solution {
    long double dp[9][25][25][9][9]={};
    long double comb[25][25]={};
public:
    double getProbability(vector<int>& balls) {
        dp[0][0][0][0][0] = 1;
        int m = balls.size();
        int n = 0;
        for (auto i: balls) n += i;
        int hf = n >> 1;
        // comb(x, y)
        for (int x = 0; x < 25; ++x){
            for (int y = 0; y <= x; ++ y){
                if (x == 0 || y == 0){
                    comb[x][y] = 1;
                    continue;
                }
                comb[x][y] = comb[x - 1][y - 1] + comb[x - 1][y];
            }
        }

        // select t-th color
        // t-1 color of balls is selected
        // [T][a][b][c][d]
        int pre = 0;
        for (int t = 1; t <= m; ++ t){
            int cur_color_num = balls[t - 1];
            for (int a = 0; a <= pre && a <=hf; ++a){
                int b = pre - a;
                if (b > hf) continue;
                for (int c = 0; c < t; ++c)
                    for (int d = 0; d < t; ++ d)
                        for (int num = 0; num <= cur_color_num; ++num){
                            if (num == 0){
                                if (b + cur_color_num > hf) continue;
                                dp[t][a][b + cur_color_num][c][d + 1] += dp[t-1][a][b][c][d] *
                                comb[b + cur_color_num][b];
                            }
                            else if(num == cur_color_num){
                                if (a + num > hf) continue;
                                dp[t][a + num][b][c + 1][d] += dp[t - 1][a][b][c][d] * comb[a + num][a];
                            }
                            else{
                                if (a + num > hf || b + cur_color_num - num > hf) continue;
                                dp[t][a + num][b + cur_color_num - num][c + 1][d + 1] += dp[t-1][a][b][c][d] * comb[a + num][a] * comb[b + cur_color_num - num][b];
                            }
                        }
                }
            pre += cur_color_num;
            }

        long double all_ = 0;
        long double cnt_ = 0;

        for(int c = 1; c <= m; ++c){
            for (int d = 1; d <= m; ++d){
                all_ += dp[m][hf][hf][c][d];
                if (c == d) cnt_ += dp[m][hf][hf][c][d];
            }
        }
        return cnt_/all_;
    }
};