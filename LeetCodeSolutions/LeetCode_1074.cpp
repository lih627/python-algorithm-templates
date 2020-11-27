class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int prefix[row][col];
        memset(prefix, 0, sizeof(prefix));
        int ret = 0;
        for(int x = 0; x < row; ++x){
            for(int y = 0; y < col; ++y){
                if (x == 0 && y == 0){
                    prefix[x][y] = matrix[x][y];
                }
                else if(x == 0){
                    prefix[x][y] = matrix[x][y] + prefix[x][y - 1];
                }
                else if(y == 0){
                    prefix[x][y] = matrix[x][y] + prefix[x - 1][y];
                }
                else prefix[x][y] = matrix[x][y] + prefix[x - 1][y] + prefix[x][y - 1] - prefix[x - 1][y - 1];
                // cout << x << ' ' << ' ' << y << ' ' << prefix[x][y] << endl;
                for (int i = 0; i <= x; ++ i){
                    for(int j = 0; j <= y; ++j){
                        int c =  i && j ? prefix[i - 1][j - 1]: 0;
                        int a = i ? prefix[i - 1][y]: 0;
                        int b = j ? prefix[x][j - 1]: 0;
                        int tmp = prefix[x][y] - a - b + c;
                        if (tmp == target) ++ ret;
                    }
                }
            }
        }
        return ret;
    }
};