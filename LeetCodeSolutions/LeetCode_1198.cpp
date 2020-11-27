class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        int row = mat.size(), col = mat[0].size();
        vector<int> pos(row, 0);
        while (true){
            int cmax = mat[0][pos[0]];
            int ccnt = 1;
            for(int i = 1; i < row; ++i){
                int &val = mat[i][pos[i]];
                if (val == cmax){
                    ++ccnt;
                }
                else if(val > cmax){
                    ccnt = 1;
                    cmax = val;
                }
            }
            if (ccnt == row) return cmax;
            for(int i = 0; i < row; ++i){
                vector<int>::iterator nxt = lower_bound(begin(mat[i]) + pos[i], end(mat[i]), cmax);
                if (nxt == end(mat[i])) return -1;
                pos[i] = nxt - begin(mat[i]);
            }
        }
        return -1;
    }
};