/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        stack<pair<TreeNode*, bool> > s;
        if(!root) return nullptr;
        s.push(make_pair(root, false));
        bool isThis = false;
        while(!s.empty()){
            auto tmp = s.top();
            s.pop();
            if(!tmp.second){
                tmp.second = true;
                if(tmp.first->right) s.push(make_pair(tmp.first->right, false));
                s.push(tmp);
                if(tmp.first->left) s.push(make_pair(tmp.first->left, false));
            }
            else{
                if(isThis) return tmp.first;
                if(tmp.first == p) isThis = true;
            }
        }
        return nullptr;
    }
};