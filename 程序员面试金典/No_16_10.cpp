class Solution {
public:
    int maxAliveYear(vector<int>& birth, vector<int>& death) {
        int max_cnt = 0, year = 0;
        int cur_cnt = 0;
        int i = 0, j = 0;
        sort(birth.begin(), birth.end());
        sort(death.begin(), death.end());
        // for (auto b: birth) cout << b << ' ' ;
        // cout << endl;
        // for (auto d: death) cout << d << ' ' ;
        // cout << endl;
        while (i < birth.size()){
            int b = birth[i], d = death[j];
            if (b <= d){
                ++cur_cnt;
                ++i;
            }
            else if(b > d){
                --cur_cnt;
                ++j;
            }
            if (cur_cnt > max_cnt) {
                max_cnt = cur_cnt;
                year = b;
            }
        }
        return year;
    }
};