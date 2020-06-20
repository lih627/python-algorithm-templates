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
    int ret = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        helper(root);
        return ret;
    }
    int helper(TreeNode *node){
        if(!node) return 0;
        int left = max(helper(node->left), 0);
        int right = max(helper(node->right),0);
        ret = max(ret, left + right + node->val);
        return max(left, right) + node->val;
    }
};