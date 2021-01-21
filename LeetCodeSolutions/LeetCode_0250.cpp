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
    int cnt;
public:
    int countUnivalSubtrees(TreeNode* root) {
        cnt = 0;
        dfs(root);
        return cnt;
    }

    bool dfs(TreeNode *node){
        if (node == nullptr) return true;
        bool l = dfs(node->left);
        bool r = dfs(node->right);
        if (!(l && r)) return false;
        int vl = node->val, vr = node->val;
        if (node->left != nullptr) vl = node->left->val;
        if (node->right != nullptr) vr = node->right->val;
        if (node->val == vl && node->val == vr){++cnt; return true;}
        return false;
    }
};