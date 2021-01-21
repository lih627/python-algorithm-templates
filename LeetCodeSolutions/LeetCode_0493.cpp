using ll = long long;
class BIT{
    private:
        vector<int> parents;
        int size;
    public:
    BIT(int sz){
        parents.resize(sz + 1, 0);
        size = sz;
    }

    constexpr int lowbit(int x){
        return x & -x;
    }

    void update(int x, int val){
        while (x <= size){
            parents[x] += val;
            x += lowbit(x);
        }
    }

    int query(int x){
        int ret = 0;
        while (x > 0){
            ret += parents[x];
            x -= lowbit(x);
        }
        return ret;
    }
};


class Solution {
public:
    int reversePairs(vector<int>& nums) {
        vector<ll> sort_nums{nums.begin(), nums.end()};
        for(auto &n: nums) sort_nums.push_back(2ll*n);
        sort(sort_nums.begin(), sort_nums.end());
        unordered_map<ll, int> num2id;
        int id = 1, i = 0;
        while (i < sort_nums.size()){
            num2id[sort_nums[i]] = id;
            ++id;
            while(i + 1< sort_nums.size() && sort_nums[i + 1] == sort_nums[i]) ++i;
            ++i;
        }
        int size = id, ans = 0;
        BIT bit(size);
        for(auto &n: nums){
            int cid = num2id[n], qid = num2id[2ll * n];
            int increase = bit.query(size) - bit.query(qid);
            ans += increase;
            bit.update(cid, 1);
        }
        return ans;
    }
};