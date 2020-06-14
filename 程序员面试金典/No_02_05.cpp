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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode res(-1);
        ListNode *p = &res;
        int carry = 0;
        while (l1 || l2 || carry){
            int a = 0, b = 0;
            a = l1? l1->val: 0;
            b = l2? l2->val: 0;
            int tmp = a + b + carry;
            carry = tmp > 9? 1: 0;
            tmp %= 10;
            p->next = new ListNode(tmp);
            p = p->next;
            l1 = l1? l1->next: l1;
            l2 = l2? l2->next: l2;
        }
        return res.next;
    }
};