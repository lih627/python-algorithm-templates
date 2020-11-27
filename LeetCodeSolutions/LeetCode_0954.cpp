bool cmp(int a, int b){
    if (a * b <= 0) return a < b;
    if (a <  0) return abs(a) < abs(b);
    return a < b;
}

class Solution {
public:
    bool canReorderDoubled(vector<int>& A) {
        sort(A.begin(), A.end(), cmp);
        for(auto v: A) cout << v << ' ';
        unordered_map<int, int> cnt;
        for(int i = 0; i < A.size(); ++i){
            if (A[i] == 0) continue;
            if (cnt[A[i]]) --cnt[A[i]];
            else ++cnt[A[i] * 2];
        }
        for(auto &kv: cnt) if (kv.second) return false;
        return true;
    }
};