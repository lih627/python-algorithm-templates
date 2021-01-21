const int maxN = 1000010;
class Solution {
    int son[maxN][2], idx;
public:
    int findMaximumXOR(vector<int>& nums) {
        memset(son, 0, sizeof(son));
        idx = 0;
        int ans = 0;
        for(int &num: nums){
            for(int i = 31, p = 0; i > -1; --i){
                int c = (num >> i) & 1;
                if (!son[p][c]) son[p][c] = ++idx;
                p = son[p][c];
            }

            int prev = 0;
            for(int i = 31, p = 0; i > -1; --i){
                int c = (num >> i) & 1;
                if (!son[p][1 - c]) {prev <<= 1; p = son[p][c];}
                else{prev <<= 1; ++prev; p = son[p][1- c];};
            }
            ans = max(prev, ans);
        }
        return ans;
    }
};