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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = findSizeOfList(head);
        if(size == 0) return head;
        if(size == 1){
            delete head;
            return NULL;
        }
        
        int index = size - n - 1;
        if(index == -1){
            ListNode* temp = head->next;
            delete head;
            return temp;
        }
        ListNode* temp = head;
        for (int i = 0; i < index; i++) temp = temp->next;
        if(index == size - 2){
            delete temp->next;
            temp->next = NULL;
        }else{
            ListNode* toDelete = temp->next;
            temp->next = toDelete->next;
            delete toDelete;
        }
        return head;        
    }
    int findSizeOfList(ListNode *head)
    {
        if(head == NULL) return 0;
        return findSizeOfList(head->next) + 1;
    }
};