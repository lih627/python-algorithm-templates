bool cmp(vector<int> &a, vector<int> &b){
    if (a[1] - a[0] > b[1] - b[0])
        return true;
    else if( a[1] - a[0] < b[1] - b[0]) return false;
    else return a[0] < b[0];
}

bool visited[1010];

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), cmp);
        int n = intervals.size();
        memset(visited, 0, sizeof(visited));
        // for(auto v: intervals){
        //     cout << v[0] << ' ' << v[1] << endl;
        // }
        int ans = 0;
        for (int i = 0; i < n; ++i){
            if (!visited[i]){
                ++ans;
                for(int j = i + 1; j < n; ++j){
                    if (!visited[j] && intervals[i][0] <= intervals[j][0] && intervals[i][1] >= intervals[j][1]){
                        visited[j] = true;
                    }
                }
            }
        }
        return ans;
    }
};