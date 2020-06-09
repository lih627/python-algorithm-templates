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
    int kthToLast(ListNode* head, int k) {
        ListNode *s = head, *f = head;
        while (k--){
            f = f->next;
        }
        while (f){
            s = s->next;
            f = f->next;
        }
        return s->val;
    }
};