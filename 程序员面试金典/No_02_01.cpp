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
    ListNode* removeDuplicateNodes(ListNode* head) {
        if (!head) return head;
        unordered_set<int> visited;
        ListNode dummy;
        dummy.val = -1;
        dummy.next = head;
        while(head){
            visited.insert(head->val);
            while (head->next && visited.count(head->next->val)) head->next = head->next->next;
            head = head->next;
        }
        return dummy.next;

    }
};