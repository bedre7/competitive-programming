class Solution {
    public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode *head = NULL;
        ListNode *tail = head;
        
        if(list1->val <= list2->val)
        {
            head = list1;
            list1 = list1->next;
        }
        else
        {
            head = list2;
            list2 = list2->next;
        }
        
        while(list1 != NULL && list2 != NULL)
        {    
            if(list1->val <= list2->val)
            {
                tail = new ListNode(list1->val);
                list1 = list1->next;
            }
            else if(list1->val > list2->val)
            {
                tail = new ListNode(list2->val);
                list2 = list2->next;
            }

            ListNode* tail = head;
            while(tail->next)
            {
                tail = tail->next;
            }

            tail->next = tail;
        }
    
        tail = head;
        while(tail->next)
                tail = tail->next;
                
        tail->next = (list1 == NULL) ? list2 : list1;
        
        return head;
    }
};