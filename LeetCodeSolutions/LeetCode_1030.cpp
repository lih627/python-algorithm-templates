int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};
bool visited[101][101];
class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        vector<vector<int>> ret;
        deque<vector<int>> que;
        que.push_back({r0, c0});
        memset(visited, 0, sizeof(visited));
        visited[r0][c0] = true;
        while(!que.empty()){
            vector<int> tmp = que.front();
            que.pop_front();
            ret.push_back(tmp);
            int x = tmp[0], y = tmp[1];
            for (int i = 0; i < 4; ++i){
                int _dx = dx[i], _dy = dy[i];
                int xx = x + _dx, yy = y + _dy;
                if (xx > -1 && xx < R && yy > -1 && yy < C && !visited[xx][yy]){
                    visited[xx][yy] = true;
                    que.push_back({xx, yy});
                }
            }
        }
        return ret;
    }
};