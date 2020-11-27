/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode *odd = new ListNode(), *even = new ListNode();
        ListNode *p = odd, *q = even, *h = head;
        bool isodd = true;
        while(h != nullptr){
            ListNode *nxt = h->next;
            if (isodd){
                p->next = h;
                h->next = nullptr;
                p = p->next;
            }
            else{
                q->next = h;
                h->next = nullptr;
                q = q->next;
            }
            isodd = !isodd;
            h = nxt;
        }
        p->next = even->next;
        delete even;
        ListNode *ret = odd->next;
        delete odd;
        return ret;
    }
};