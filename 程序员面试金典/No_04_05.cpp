/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 typedef long long int ll;
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return __isValid(root, LONG_MAX , LONG_MIN);
    }

    bool __isValid(TreeNode *root, ll hi, ll lo){
        if(!root) return true;
        if(!(root->val < hi) || !(root->val > lo)) return false;
        return __isValid(root->left, root->val, lo) && __isValid(root->right, hi, root->val);
    }
};