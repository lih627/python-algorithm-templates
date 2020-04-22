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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        deque<TreeNode*> que = {root};
        while (que.size()){
            auto sz = que.size();
            for(int i=0; i!=sz;++i){
                TreeNode *node = que.front();
                que.pop_front();
                if (node != NULL) {
                    if (i + 1== sz) res.push_back(node->val);
                    if (node->left) que.push_back(node->left);
                    if (node->right) que.push_back(node->right);
                }
            }
        }
        return res;


    }
};