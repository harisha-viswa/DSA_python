'''
. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''
from typing import Optional

class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
'''In Python typing, Optional[X] means:
This value can be either of type X or it can be None.

The input head might be a ListNode, or it might be None (empty list).

The function returns either a ListNode (if the list exists) or None (if it was empty).

if not used gives run time error
'''
class Solution:
    def deleteDuplicates(self, head: Optional[listNode]) -> Optional[listNode]:
        curr=head
        while curr:
            while curr.next and curr.next.val==curr.val:
                curr.next=curr.next.next
            curr=curr.next
        return head
# Helper to convert list to linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = listNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = listNode(val)
        curr = curr.next
    return head

# Helper to convert linked list to list (for printing)
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


nums = [1, 1, 2, 3, 3]
linked = list_to_linkedlist(nums)
result = Solution().deleteDuplicates(linked)
print(linkedlist_to_list(result))
