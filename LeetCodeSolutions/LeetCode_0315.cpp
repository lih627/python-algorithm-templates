class BIT{
    public:
    vector<int> bit;
    BIT(int n){
        bit.resize(n, 0);
    }
    inline int lowbit(int x){return x & -x;}
    int query(int x){
        int ret = 0;
        x -= 1;
        while(x  >= 1){
            ret += bit[x];
            x -= lowbit(x);
        }
        return ret;
    }

    void update(int x){
        while (x < bit.size()){
            ++bit[x];
            x += lowbit(x);
        }
    }

};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> tmp(nums.begin(), nums.end());
        sort(tmp.begin(), tmp.end());
        unordered_map<int, int> n2id;
        int cnt = 1;
        for(int i = 0; i < tmp.size(); ++i){
            if (i > 0 && tmp[i] == tmp[i - 1]) continue;
            n2id[tmp[i]] = cnt++;
        }
        BIT bit(cnt);
        vector<int> ret;
        for(int i = nums.size() - 1; i >=0; --i){
            int uid = n2id[nums[i]];
            ret.push_back(bit.query(uid));
            bit.update(uid);
        }
        return {ret.rbegin(), ret.rend()};

    }
};