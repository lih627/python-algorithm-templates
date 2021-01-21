typedef pair<int, char> PIC;

struct cmp{
    bool operator() (const pair<int, char> &a, const pair<int, char> &b) const{
        return a.first < b.first;
    }
};

class Solution {
public:
    string reorganizeString(string S) {
        int cnt[26] = {};
        for (char c: S) ++cnt[c - 'a'];
        int m = 0;
        for(int i = 0; i < 26; ++i) m = max(cnt[i], m);
        int len = S.size();
        if (m > (len + 1) / 2) return {};
        priority_queue<PIC, vector<PIC>, cmp> pq;
        for (int i =0; i < 26; ++i){
            pq.push(make_pair(cnt[i], 'a' + i));
        }
        string ret;
        while (!pq.empty()){
            auto f = pq.top();
            pq.pop();
            if (f.first){
                ret += f.second;
                --f.first;
            }
            if (!pq.empty()){
                auto s = pq.top();
                pq.pop();
                if (s.first){
                    ret += s.second;
                    --s.first;
                }
                if (f.first) pq.push(f);
                if (s.first) pq.push(s);
            }
            else if (f.first) pq.push(f);
        }
        return ret;
    }
};