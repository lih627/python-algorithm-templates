class Solution {
public:
    int smallestDifference(vector<int>& a, vector<int>& b) {
        using ll = long long;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int l = 0, r = 0;
        ll ret = abs(ll(a[0]) - b[0]);
        int na = a.size(), nb = b.size();
        while (l < na && r < nb){
            ret = min(ll(ret), abs(ll(a[l]) - b[r]));
            if (a[l] < b[r])++l;
            else if(a[l] > b[r])++r;
            else break;
        }
        return ret;
    }
};