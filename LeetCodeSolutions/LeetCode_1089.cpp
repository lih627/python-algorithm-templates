class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        bool copy_twice = false;
        int last_idx = 0;
        int cnt = 0;
        while (cnt < n){
            if (arr[last_idx]){
                ++cnt;
            }
            else{
                cnt += 2;
            }
            if (cnt == n){
                copy_twice = true;
                break;
            }
            if(cnt > n) break;
            ++last_idx;
        }
        // cout << last_idx ;
        --n;
        if (arr[last_idx] == 0){
            --last_idx;
            if (copy_twice){
                arr[n] = 0;
                arr[n - 1] = 0;
                n -= 2;
            }
            else{
                arr[n] = 0;
                --n;
            }
        }
        while(n > -1){
            if (arr[last_idx]){
                arr[n] = arr[last_idx];
                --n;
            }
            else{
                arr[n] = 0;
                arr[n - 1] = 0;
                n -= 2;
            }
            --last_idx;
        }
    }
};