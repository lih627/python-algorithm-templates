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
    int ret;
public:
    int largestBSTSubtree(TreeNode* root) {
        ret = 0;
        dfs(root);
        return ret;
    }

    vector<int> dfs(TreeNode *node){
        // valid, num, min, max
        if (node == nullptr)
            return {1, 0, INT_MAX, INT_MIN};
        vector<int> left = dfs(node->left);

        vector<int> right = dfs(node->right);
        if (left[0] == 0 || right[0] == 0){
            return {0, 0, 0, 0};
        }

        if (node->val > left[3] && node->val < right[2]){
            ret = max(ret, left[1] + right[1] + 1);
            int l = left[1] == 0? node->val: left[2];
            int r = right[1] == 0? node->val: right[3];
            // cout << node->val << ' ' << left[1] + right[1] + 1 << ' ' << l << ' '<< r<< endl;
            return {1, left[1] + right[1] + 1, l, r};
        }
        else return {0, 0, 0, 0};
    }

};