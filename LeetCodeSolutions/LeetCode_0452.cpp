bool cmp(const vector<int> &a, const vector<int> & b){
    return a[1] < b[1];
}

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        sort(points.begin(), points.end(), cmp);
        int cnt = 1;
        int r = points[0][1];
        for(auto &p: points){
            if (p[0] > r){
                ++cnt;
                r = p[1];
            }
        }
        return cnt;
    }
};