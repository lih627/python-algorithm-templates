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
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        auto t = helper(root, 0, limit);
        if (t < limit) return nullptr;
        return root;
    }

    int helper(TreeNode *node, int val, int &limit){

        if (node == nullptr) return val;
        if (node->left == nullptr && node->right == nullptr) return node->val + val;
        if (node->left != nullptr && node->right != nullptr){
            int left = helper(node->left, node->val + val, limit);
            int right = helper(node->right, node->val + val, limit);
            if (left < limit)
                node->left = nullptr;
            if (right < limit)
                node->right = nullptr;
            return max(left, right);
        }
        else if (node->left != nullptr){
            int left = helper(node->left, node->val + val, limit);
            if (left < limit)
                node->left = nullptr;
            return left;
        }
        else if (node->right != nullptr){
            int right = helper(node->right, node->val + val, limit);
            if (right < limit)
                node->right = nullptr;
            return right;
        }
        return 0;
    }
};