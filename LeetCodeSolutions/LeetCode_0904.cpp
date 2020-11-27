class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int ret = 0, l = 0, r = 0;
        unordered_map<int, int> counter;
        while (r < tree.size()){
            ++counter[tree[r]];
            while (counter.size() > 2){
                --counter[tree[l]];
                if(counter[tree[l]] == 0) counter.erase(tree[l]);
                ++l;
            }
            ret = max(ret, r - l + 1);
            ++r;
        }
        return ret;
    }
};