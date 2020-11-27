class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> mp;
        for(auto &n: arr2) mp[n] = 0;
        vector<int> tmp;
        for(auto &n: arr1) {
            if(mp.count(n)) ++mp[n];
            else tmp.push_back(n);
        }
        sort(tmp.begin(), tmp.end());
        vector<int> ret;
        for(auto n: arr2){
            while(mp[n]){
                ret.push_back(n);
                --mp[n];
            }
        }
        ret.insert(ret.end(), tmp.begin(), tmp.end());
        return ret;
    }
};