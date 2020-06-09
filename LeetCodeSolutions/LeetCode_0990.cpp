class DSU{
    public:
    unordered_map<int, int> parent;

    int find(int i){
        if (!parent.count(i)) parent[i] = i;
        while (parent[i] != i){
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        return i;
    }

    void union_(int a, int b){
        int a_root = find(a);
        int b_root = find(b);
        if (a_root != b_root){
            parent[a_root] = b_root;
        }
    }

    bool isEqual(int a, int b){
        return find(a) == find(b);
    }

};

class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        DSU dsu;
        vector<pair<int, int> > nequals;
        for (string &s: equations){
            if (s[1] == '='){
                dsu.union_(int(s[0] - 'a'), int(s[3] - 'a'));
            }
            else nequals.push_back(make_pair(s[0] - 'a', s[3] - 'a'));
        }
        for (auto &p: nequals){
            if (dsu.isEqual(p.first, p.second)) return false;
        }
        return true;
    }
};