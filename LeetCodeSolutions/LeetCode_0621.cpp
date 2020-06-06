class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int nums = tasks.size();
        vector<int> counter(26, 0);
        for (char s: tasks) ++counter[s - 'A'];
        sort(counter.begin(), counter.end(), greater<int>());
        int cnt = 1;
        while (cnt < counter.size() && counter[cnt] == counter[0]) ++cnt;
        return max(nums, cnt + (n + 1) * (counter[0] - 1));
    }
};

// or use lambda
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int nums = tasks.size();
        vector<int> counter(26, 0);
        for (char s: tasks) ++counter[s - 'A'];
        sort(counter.begin(), counter.end(),[](const int&a, const int &b){return a > b;});
        int cnt = 1;
        while (cnt < counter.size() && counter[cnt] == counter[0]) ++cnt;
        return max(nums, cnt + (n + 1) * (counter[0] - 1));
    }
};