/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class CBTInserter {
    deque<TreeNode*> nodes;
public:
    CBTInserter(TreeNode* root) {
        deque<TreeNode*> tmp;
        tmp.emplace_back(root);
        while(!tmp.empty()){
            auto t = tmp.front();
            tmp.pop_front();
            // cout << t->val << endl;
            nodes.emplace_back(t);
            if(t->left != nullptr) tmp.emplace_back(t->left);
            if(t->right != nullptr) tmp.emplace_back(t->right);
        }
    }

    int insert(int v) {
        int sz = nodes.size();
        TreeNode *n = new TreeNode(v);
        nodes.emplace_back(n);
        int prev = (sz - 1) / 2;
        if (sz%2){
            nodes[prev]->left = nodes.back();
        }
        else{
            nodes[prev]->right = nodes.back();
        }
        // cout << nodes[prev]->val << endl;
        return nodes[prev]->val;
    }

    TreeNode* get_root() {
        return nodes.front();
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(v);
 * TreeNode* param_2 = obj->get_root();
 */