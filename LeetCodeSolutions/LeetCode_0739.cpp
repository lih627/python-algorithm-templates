class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        vector<int > res(n, 0);
        vector<pair<int, int>> stack;
        for(int i = n - 1; i > -1; --i){
            while (!stack.empty() && T[i] >= stack.back().first) stack.pop_back();
            if(stack.empty()) res[i] = 0;
            else res[i] = stack.back().second - i;
            stack.push_back(make_pair(T[i], i));
        }
        return res;

    }
};