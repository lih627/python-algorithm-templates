/*
 * @lc app=leetcode.cn id=404 lang=cpp
 *
 * [404] 左叶子之和
 */

// @lc code=start
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
    int ret;
public:
    int sumOfLeftLeaves(TreeNode* root) {
        ret = 0;
        dfs(root);
        return ret;
    }
    bool isLeaf(TreeNode *node){
        return node && !node->left && !node->right;
    }

    void dfs(TreeNode *node){
        if (!node) return;
        if (isLeaf(node->left)) ret += node->left->val;
        dfs(node->left);
        dfs(node->right);
    }
};
// @lc code=end

