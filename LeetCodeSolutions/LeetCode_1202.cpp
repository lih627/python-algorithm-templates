const int M = 100010;

int parent[M];

int find(int x){
    return parent[x] == x? x: parent[x] = find(parent[x]);
}

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        for(int i = 0; i < n; ++i) parent[i] = i;
        for(auto &p: pairs){
            int rx = find(p[0]);
            int ry = find(p[1]);
            parent[ry] = rx;
        }
        vector<vector<char>> v(n);
        for(int i = 0; i < n; ++i){
            v[find(i)].push_back(s[i]);
        }
        for(auto &m: v){
            sort(m.begin(), m.end());
            reverse(m.begin(), m.end());
        }
        string ret;
        for(int i = 0; i < n; ++i){
            ret += v[find(i)].back();
            v[find(i)].pop_back();
        }
        return ret;
    }
};