# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = self.reverseList(slow.next)
        slow.next = None
        
        while fast:
            temp, temp2 = head.next, fast.next
            head.next = fast
            fast.next = temp
            head = temp
            fast = temp2




    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # temp = next node
            curr.next = prev # change current node next to previous
            prev = curr # move previous to current
            curr = temp # move current to next node
        return prev