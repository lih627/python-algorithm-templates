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

typedef pair<unsigned long long, unsigned long long> PII;

class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        unordered_map<int, PII> mp;
        helper(root, 0, 0, mp);
        unsigned long long ans = 0;
        for(auto &p: mp) ans = max(ans, p.second.second - p.second.first + 1);
        return ans;
    }

    void helper(TreeNode *node,  unsigned long long id, int depth, unordered_map<int, PII>& mp){
        if (node == nullptr) return ;
        if (mp.count(depth)){
            mp[depth].first = min(id, mp[depth].first);
            mp[depth].second = max(mp[depth].second, id);
        }
        else{
            mp[depth] = make_pair(id, id);
        }
        if (node->left != nullptr)
            helper(node->left, id * 2, depth + 1, mp);
        if (node->right != nullptr)
            helper(node->right, id * 2 + 1, depth + 1, mp);
    }
};