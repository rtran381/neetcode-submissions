# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        head = dummy
        while l1 or l2 or carry:
            v1,v2 = 0, 0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val

            newValue = v1 + v2 + carry
            carry = newValue // 10
            newValue = newValue % 10

            head.next = ListNode(newValue)
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        
