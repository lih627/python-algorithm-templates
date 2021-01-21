typedef pair<int, int> PII;

struct cmp{
    bool operator()(const PII &a, const PII &b) const{
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second;
    }
};

class Solution {
public:
    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        vector<PII> hw;
        for(int i = 0; i < height.size(); ++i)
            hw.emplace_back(height[i], weight[i]);
        sort(hw.begin(), hw.end(), cmp());
        vector<int> stack;
        for (auto &p: hw){
            if (stack.empty() || p.second > stack.back()){
                stack.push_back(p.second);
            }
            else{
                auto it = lower_bound(stack.begin(), stack.end(), p.second);
                *it = p.second;
            }
        }
        return stack.size();
    }
};