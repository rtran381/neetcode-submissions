# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # temp = next node
            curr.next = prev # change current node next to previous
            prev = curr # move previous to current
            curr = temp # move current to next node
        return prev
            
