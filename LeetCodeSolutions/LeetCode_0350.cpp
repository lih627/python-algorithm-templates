class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ret;
        unordered_map<int, int> counter;
        for(auto &n: nums1) ++counter[n];
        for(auto &n: nums2){
            if(counter[n] > 0){
                --counter[n];
                ret.push_back(n);
            }
        }
        return ret;

    }
};