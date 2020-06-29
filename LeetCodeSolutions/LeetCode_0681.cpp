class Solution {
public:
    string nextClosestTime(string time) {
        vector<int> idxs{0, 1, 3, 4};
        vector<char> uppbound{'2', '3', '5', '9'};
        set<char> nums;
        for(auto &n: idxs) nums.insert(time[n]);

        if(nums.size() == 1) return time;

        string ret = time;
        for(int i = idxs.size() - 1; i >= 0 ; --i){
            int id = idxs[i];
            auto nxt = nums.upper_bound(ret[id]);
            if(nxt == nums.end()) continue;
            if(id != 1){
                if(*nxt <= uppbound[i]){
                    ret[id] = *nxt;
                    for(int j = i + 1; j < idxs.size(); ++j){
                        ret[idxs[j]] = *nums.begin();
                    }
                    return ret;}
            }
            else{
                if(ret[0] != '2'){
                    ret[id] = *nxt;
                    for(int j = i + 1; j < idxs.size(); ++j){
                        ret[idxs[j]] = *nums.begin();
                    }
                    return ret;
                }
                else{
                    if(*nxt <= uppbound[i]){
                        ret[id] = *nxt;
                        for(int j = i + 1; j < idxs.size(); ++j){
                            ret[idxs[j]] = *nums.begin();
                        }
                        return ret;}
                }
            }
        }

        for(auto id: idxs){
            ret[id] = *nums.begin();
        }
        return ret;
    }
};