class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }
    void print(vector<int> & nums){
        for(auto n: nums)
            cout << n << ' ';
        cout << endl;
    }

    int quickSelect(vector<int> &a, int l, int r, int k){
        randomPartition(a, l, r);
        int p = Partition(a, l, r);
        // print(a);
        if(p == k) return a[p];
        return p < k? quickSelect(a, p + 1, r, k) : quickSelect(a, l, p - 1, k);
    }

    void randomPartition(vector<int> &a, int l, int r){
        int k = rand() % (r - l + 1) + l;
        swap(a[r], a[k]);
    }

    int Partition(vector<int>& a, int l, int r) {
        int x = a[r], i = l - 1;
        for (int j = l; j < r; ++j) {
            if (a[j] <= x) {
                swap(a[++i], a[j]);
            }
        }
        swap(a[i + 1], a[r]);
        return i + 1;
    }
};