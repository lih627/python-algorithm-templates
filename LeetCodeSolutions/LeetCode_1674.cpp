class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        for(int i = 0; i < n / 2; ++i)
            if (nums[i] < nums[n - 1 - i])
                swap(nums[i], nums[n - 1 - i]);

        vector<int> arr(limit * 2 + 2, 0);
        for (int i = 0; i < n / 2; ++i){
            int lo = nums[n - 1 - i], hi = nums[i];
            --arr[lo + 1];
            --arr[lo + hi];
            ++arr[lo + hi + 1];
            ++arr[hi + limit + 1];
        }
        int ans = n;
        int now = n;
        for(auto k: arr){
            now += k;
            ans = min(ans, now);
        }
        return ans;
    }
};