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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr) return head;
        ListNode *slow = head, *fast = head->next;
        if (fast == nullptr){
            return head;
        }
        while (fast!= nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next;
            if(fast != nullptr) fast = fast->next;
        }
        ListNode *right = slow->next;
        slow->next = nullptr;
        return merge(sortList(head), sortList(right));
    }

    ListNode *merge(ListNode *left, ListNode *right){
        ListNode *dummy = new ListNode(0);
        ListNode *p = dummy;
        while(left != nullptr && right != nullptr){
            if (left->val <= right->val){
                p->next = left;
                p = p->next;
                left = p->next;
                p->next = nullptr;
            }
            else{
                p->next = right;
                p = p->next;
                right = p->next;
                p->next = nullptr;
            }
        }
        if (left != nullptr){
            p->next = left;
        }
        if (right != nullptr){
            p->next = right;
        }
        p = dummy->next;
        delete dummy;
        dummy = nullptr;
        return p;
    }



};