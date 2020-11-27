const int one_day = 24 * 60;
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> tmp;
        for (auto &s: timePoints){
            int h = 0, m = 0;
            h += s[0] - '0';
            h *= 10;
            h += s[1] - '0';
            m += s[3] - '0';
            m *= 10;
            m += s[4] - '0';
            tmp.push_back(h * 60 + m);
        }
        sort(tmp.begin(), tmp.end());
        int ret = one_day - (tmp.back() - tmp.front());
        for(int i = 0; i < tmp.size() - 1; ++i)
            ret = min(ret, tmp[i + 1] - tmp[i]);
        return ret;
    }
};