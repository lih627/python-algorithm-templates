/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        unordered_set<int> st;
        while(p != nullptr){
            st.insert(p->val);
            p = p->parent;
        }
        while (q != nullptr){
            if (st.count(q->val))
                return q;
            q = q->parent;
        }
        return nullptr;
    }
};