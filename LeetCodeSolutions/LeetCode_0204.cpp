bool visited[5000010];

class Solution {
public:
    int countPrimes(int n) {
        memset(visited, 0, sizeof(visited));
        int cnt = 0;
        for(int i = 2; i < n; ++i){
            if (!visited[i]){
                ++cnt;
                int k = 2;
                while (i * k < n){
                    visited[i * k] = true;
                    ++k;
                }
            }
        }
        return cnt;
    }
};