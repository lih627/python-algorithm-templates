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
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return helper(0, n + 1);
    }

    vector<TreeNode*> helper(int lo, int hi){
        if (lo + 1 >= hi) return {nullptr};
        vector<TreeNode*> ret;
        for(int val = lo + 1; val < hi; ++val){
            auto left = helper(lo, val);
            auto right = helper(val, hi);
            for(auto l: left){
                for(auto r: right){
                    auto root = new TreeNode(val);
                    root->left = l;
                    root->right = r;
                    ret.push_back(root);
                }
            }
        }
        return ret;
    }
};