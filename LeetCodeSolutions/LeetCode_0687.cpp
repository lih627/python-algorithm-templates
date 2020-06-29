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
    int ans;
public:
    int longestUnivaluePath(TreeNode* root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    int dfs(TreeNode *node){
        if(!node) return 0;
        int l = dfs(node->left), r = dfs(node->right);
        int tmp = 0;
        if(node->left && node->left->val == node->val)  tmp += ++l;
        else l = 0;
        if(node->right && node->right->val == node->val)tmp += ++r;
        else r = 0;
        ans = max(ans, tmp);
        return max(l, r);

    }
};