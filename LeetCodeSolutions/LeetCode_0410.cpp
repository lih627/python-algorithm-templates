class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long long l = 0, r = 0;
        for(auto &n: nums){
            r += n;
        }
        long long ret = -1;
        while (l <= r){
            long long mid = l + (r - l) / 2;
            if (check(nums, m, mid)){
                if (ret == -1) ret = mid;
                else ret = min(ret, mid);
                r = mid - 1;
            }
            else l = mid + 1;
        }
        return ret;
    }

    bool check(vector<int> &nums, int m, long long sum){
        int cnt = 1;
        long long cur_sum = 0;
        for (auto &n: nums){
            if (n > sum) return false;
            cur_sum += n;
            if(cur_sum > sum){
                ++cnt;
                cur_sum = n;
            }
        }
        // cout << m << ' ' << sum << ' ' << cnt;
        return cnt <= m;
    }
};