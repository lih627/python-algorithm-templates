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
    void deleteNode(ListNode* node) {
        ListNode *pre = node;
        while (node->next){
            pre = node;
            node->val = node->next->val;
            node = node->next;
        }
        pre->next = nullptr;
    }
};