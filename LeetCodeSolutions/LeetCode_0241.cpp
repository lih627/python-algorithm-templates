class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<char> ops;
        vector<int> nums;
        int i = 0;
        while (i < input.size()){
            int num = 0;
            if (input[i] >= '0' && input[i] <= '9'){
                while ( i < input.size() && input[i] >= '0' && input[i] <= '9'){
                    num *= 10;
                    num += input[i] - '0';
                    ++i;
                }
                nums.push_back(num);
            }
            else{
                ops.push_back(input[i]);
                ++i;
            }
        }
        return helper(ops, nums);
    }

     vector<int> helper(vector<char> ops, vector<int> nums){
        if (ops.size() == 0) return nums;
        vector<int> ret;
        for(int i = 0; i < ops.size(); ++i){
            auto l = helper({ops.begin(), ops.begin() + i},
                {nums.begin(), nums.begin() + i + 1});
            auto r = helper({ops.begin() + i + 1, ops.end()},
                {nums.begin() + i + 1, nums.end()});
            char c = ops[i];
            if (c == '+'){
                for (auto a: l)
                    for (auto b: r) ret.push_back(a + b);
            }
            else if (c == '-'){
                for (auto a: l)
                    for (auto b: r) ret.push_back(a - b);
            }
            else if (c == '*'){
                for (auto a: l)
                    for (auto b: r) ret.push_back(a * b);
            }
        }
        return ret;
    }
};