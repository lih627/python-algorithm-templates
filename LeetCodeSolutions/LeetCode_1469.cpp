/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    vector<int> ret;
public:
    vector<int> getLonelyNodes(TreeNode* root) {
        if (!root) return {};
        dfs(root);
        return ret;
    }

    void dfs(TreeNode * node){
        if (!node) return;
        if (node -> left && node->right){
            dfs(node->left);
            dfs(node->right);
            return ;
        }
        if (node->left){
            ret.push_back(node->left->val);
            dfs(node->left);
        }
        if (node->right){
            ret.push_back(node->right->val);
            dfs(node->right);
        }
    }

};