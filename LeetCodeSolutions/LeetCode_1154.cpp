class Solution {
public:
    int dayOfYear(string date) {
        int months[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int year = stoi(date.substr(0, 4)), month = stoi(date.substr(5, 2)), day = stoi(date.substr(8, 2));
        bool isleap = false;
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) isleap = true;
        if (isleap) ++months[2];
        int ret = 0;
        for(int i = 1; i < month; ++i) ret += months[i];
        ret += day;
        return ret;
    }
};