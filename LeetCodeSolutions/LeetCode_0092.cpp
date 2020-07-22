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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *dummy = new ListNode(1);
        dummy->next = head;
        ListNode *pre = dummy;
        ListNode *cur = head;
        ListNode *next = cur->next;
        for(int i = 1; i < n; ++i){
            if (i < m){
                pre = cur;
                cur = cur->next;
                if(cur) next = cur->next;
            }
            else{
                ListNode *nn = next->next;
                next->next = pre->next;
                pre->next = next;
                cur->next = nn;
                next = nn;
            }
        }
        return dummy->next;
    }
};