/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> listOfDepth(TreeNode* tree) {
        if (!tree) return {};
        vector<ListNode*> ret;
        deque<TreeNode*> que;
        que.push_back(tree);
        while (!que.empty()){
            int n = que.size();
            ListNode dummy(-1);
            ListNode* p = &dummy;
            for(int i = 0; i < n; ++i){
               TreeNode* node = que.front();
               que.pop_front();
               p->next = new ListNode(node->val);
               p = p->next;
               if(node->left) que.push_back(node->left);
               if(node->right) que.push_back(node->right);
            }
            ret.push_back(dummy.next);
        }
        return ret;
    }
};