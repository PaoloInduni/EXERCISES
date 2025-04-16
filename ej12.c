/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
    int val;
    struct ListNode *next;
};

 struct ListNode* reverseList(struct ListNode* head){
    
    struct ListNode* prev = head;
    struct ListNode* cur = prev->next;
    struct ListNode* next = cur->next;

    head->next = NULL;

    while(cur != NULL){
        
        next = cur->next;

        cur->next = prev;

        prev = cur;
        cur = next;
    }

    return prev;

}