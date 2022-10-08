#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        string num1 = "", num2 = "";
        while(l1 != NULL)
        {
            num1 += to_string(l1->val);   
            l1 = l1->next;
        }
        while(l2 != NULL)
        {
            num2 += to_string(l2->val);   
            l2 = l2->next;
        }
        size_t maxLength = max(num1.length(), num2.length());
        
        string num1Str = num1 + string(maxLength - min(maxLength, num1.length()), '0');
        string num2Str = num2 + string(maxLength - min(maxLength, num2.length()), '0');

        int length = num1.length() >= num2.length() ? num1.length() : num2.length();

        int carry = 0;
        string strSum = "";

        for(int i = 0; i < length; i++)
        {
            int sum = ((num1Str[i] - '0') + (num2Str[i] - '0'));
            strSum += to_string((sum + carry) % 10);
            cout << (sum % 10) + carry << endl;
            carry = (sum + carry)/ 10;
        }
        if(carry) strSum += to_string(carry);

        ListNode *head = new ListNode(strSum[0] - '0');
        ListNode *itr = head;
        for(int i = 1; i < strSum.length(); i++)
        {
            ListNode *tmp = new ListNode(strSum[i] - '0');
            itr->next = tmp;
            itr = itr->next;  
        }
        return head;
    }
};
int main()
{
    Solution sol;
    ListNode* one = new ListNode(9);
    ListNode* two = new ListNode(4);
    ListNode* three = new ListNode(3);
    // one->next = two;
    // two->next = three;

    ListNode* four = new ListNode(9);
    ListNode* five = new ListNode(9);
    ListNode* six = new ListNode(9);
    four->next = five;
    five->next = six;
    ListNode* test = sol.addTwoNumbers(one, four);
    while(test)
    {
        cout << test->val << " ";
        test = test->next;
    }
    return 0; 
}