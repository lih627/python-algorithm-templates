/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    Node* findRoot(vector<Node*> tree) {
        int n = 0;
        for (auto &t: tree){
            n ^= t->val;
            for(auto &v: t->children) n ^= v->val;
        }
        for(auto &t: tree) if(t->val == n) return t;
        return nullptr;
    }
};