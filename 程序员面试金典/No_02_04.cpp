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
    ListNode* partition(ListNode* head, int x) {
        if (!head || !head->next) return head;
        ListNode dummy;
        dummy.val = -1;
        dummy.next = head;
        ListNode *node = head, *pre_node = &dummy, *cur_node = &dummy;
        while (node){
            if (node->val < x){
                if(cur_node != pre_node){
                    pre_node->next = node->next;
                    node->next = cur_node->next;
                    cur_node->next = node;

                    cur_node = cur_node->next;
                    node = pre_node->next; }
                else{
                    pre_node = pre_node->next;
                    node = node->next;
                }
            }
            else{
                pre_node = pre_node->next;
                node = node->next;
            }
        }
        return dummy.next;
    }
};