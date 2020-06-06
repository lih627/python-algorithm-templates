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
    int maxl = 0;
public:
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        maxl = 0;
        dfs(root, 0, root->val);
        return maxl;
    }

    void dfs(TreeNode *node, int curl, int prev){
        if (!node){
            maxl = max(maxl, curl);
            return ;
        }
        if (node->val - 1 == prev) ++curl;
        else{
            maxl = max(maxl, curl);
            curl = 1;
        }
        dfs(node->left, curl, node->val);
        dfs(node->right, curl, node->val);
    }


};