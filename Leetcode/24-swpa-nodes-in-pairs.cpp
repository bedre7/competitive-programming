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
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next) return head;
        
        ListNode* prevguy = NULL, *nextguy = head->next, *curr = head;
        
        while(nextguy && curr){
            curr->next = nextguy->next;
            nextguy->next = curr;
            if(prevguy) prevguy->next = nextguy;
            else head = nextguy;
            prevguy = curr;
            curr = curr->next;
            nextguy = curr ? curr->next : NULL;
        }
        
      return head;
    }
};