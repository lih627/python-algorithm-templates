#include <vector>
#include <utility>
#include <iostream>
#include <set>
using namespace std;
/*
 * @lc app=leetcode.cn id=327 lang=cpp
 *
 * [327] 区间和的个数
 */

// @lc code=start
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if (nums.size() == 0) return 0;
        multiset<long long> cnt;
        long long prefix = 0;
        cnt.insert(prefix);
        int ret = 0;
        for(auto num: nums){
            prefix += num;
            ret += distance(cnt.lower_bound(prefix - upper), cnt.upper_bound(prefix - lower));
            cnt.insert(prefix);
        }
        return ret;
    }
};




class BIT{
    vector<int> tree;
    int n;
public:
    BIT(int sz): n(sz), tree(sz + 1){}

    static constexpr int lowbit(int n){
        return n & -n;
    }

    void update(int idx, int val){
        while (idx <= n){
            tree[idx] += val;
            idx += lowbit(idx);
        }
    }

    int query(int idx){
        int ret = 0;
        while (idx) {
            ret += tree[idx];
            idx -= lowbit(idx);
        }
        return ret;
    }
};

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        vector<long long> preSum{0};
        long long sum = 0;
        for(int &num: nums){
            sum += num;
            preSum.push_back(sum);
        }

        set<long long> numbers;
        for(long long num: preSum){
            numbers.insert(num);
            numbers.insert(num - lower);
            numbers.insert(num - upper);
        }

        unordered_map<long long, int> mp;
        int idx = 1;
        for (auto num: numbers){
            mp[num] = idx;
            idx += 1;
        }

        int ans = 0;

        BIT  bit(mp.size());
        for (auto num: preSum){
            int left = mp[num - upper];
            int right = mp[num - lower];
            ans += bit.query(right) - bit.query(left - 1);
            bit.update(mp[num], 1);
        }
        return ans;
    }
};

// @lc code=end

