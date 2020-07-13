/*
 * @lc app=leetcode.cn id=112 lang=cpp
 *
 * [112] 路径总和
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
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) return false;
        return helper(root, 0, sum);
    }

    bool helper(TreeNode *node, int cur_sum, int &sum){
        if(!node) return false;
        if (!node->left && !node->right) return cur_sum + node->val == sum;
        return helper(node->left, cur_sum + node->val, sum) || helper(node->right, cur_sum + node->val, sum);
    }
};
// @lc code=end

