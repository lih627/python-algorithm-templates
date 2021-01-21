class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> ret(n, 0);
        for (auto &b: bookings){
            ret[b[0] - 1] += b[2];
            if (b[1] < n){
                ret[b[1]] -= b[2];
            }
        }
        for(int i = 1; i < n; ++i) ret[i] += ret[i - 1];
        return ret;
    }
};