struct node{
    int x, y, dis;
    bool operator < (const node & a) const{
        return a.dis > dis;
    }
};

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        priority_queue<node> q;
        for (auto p: points){
            q.push({p[0], p[1], p[0] * p[0] + p[1] * p[1]});
            if (q.size() > K){
                q.pop();
            }
        }
        vector<vector<int> > ret;
        while(!q.empty()){
            auto q_ = q.top();
            q.pop();
            ret.push_back({q_.x, q_.y});
        }
        return ret;
    }
};