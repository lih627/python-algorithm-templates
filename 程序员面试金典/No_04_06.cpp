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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        deque<pair<TreeNode*, bool> > que;
        que.push_back(make_pair(root, false));
        bool next = false;
        while (!que.empty()){
            auto pii = que.back();
            que.pop_back();
            if(!pii.second){
                pii.second = true;
                auto node = pii.first;
                if(node->right) que.push_back(make_pair(node->right, false));
                // cout << pii.first->val << ' ' << pii.second << endl;
                que.push_back(pii);
                if(node->left) que.push_back(make_pair(node->left, false));
                }
            else{
                // cout << pii.first->val <<endl;
                if(next) return pii.first;
                if(pii.first == p) next = true;
            }
        }
        return nullptr;
    }
};