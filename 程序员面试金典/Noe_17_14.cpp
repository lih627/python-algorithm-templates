class Solution {
public:
    vector<int> smallestK(vector<int>& arr, int k) {
        if (k == 0) return {};
        return helper(arr, 0, arr.size() - 1, k);
    }

    vector<int> helper(vector<int> & arr, int l, int r, int k){
        int p = partition(arr, l, r);
        cout << p << endl;
        if (p + 1 == k){
            vector<int> ret;
            for(int i = 0; i < k; ++i) ret.push_back(arr[i]);
            return ret;
        }
        return p + 1 < k? helper(arr, p  + 1, r, k): helper(arr, l, p - 1, k);
    }

    int partition(vector<int> &arr, int l, int r){
        int x = arr[r];
        int i = l - 1;
        for(int j = l; j < r; ++j){
            if (arr[j] < x) swap(arr[++i], arr[j]);
        }
        swap(arr[r], arr[i + 1]);
        return i + 1;
    }
};