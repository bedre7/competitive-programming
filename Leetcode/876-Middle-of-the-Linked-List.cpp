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
    ListNode* middleNode(ListNode* head) {
        int length = getLength(head);
        ListNode* temp = head;
        for (int i = 0; i < length / 2; i++, temp = temp->next);
        
        return temp;
    }
    int getLength(ListNode* head, int length = 0){
        if (head == NULL)
            return length;
        return getLength(head->next, length + 1);
    }
};