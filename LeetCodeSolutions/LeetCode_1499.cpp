class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        typedef pair<int, int > PII;
        priority_queue<PII> q;
        // yj + xj + yi - xi
        int ret = INT_MIN;
        for(auto point: points){
            if(q.empty()) q.push(make_pair(point[1] - point[0], point[0]));
            else{
                int cur_sum = point[0] + point[1];
                // cout << q.top().second << endl;
                while(!q.empty() && point[0] - q.top().second > k) q.pop();
                if(!q.empty()){
                    ret = max(ret, q.top().first + cur_sum);
                }
                q.push(make_pair(point[1] - point[0], point[0]));
            }
        }
        return ret;

    }
};