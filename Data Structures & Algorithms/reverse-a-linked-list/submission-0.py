# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        nextNode = head.next

        if nextNode == None:
            return head

        head.next = None
        next2 = nextNode.next

        while nextNode != None:
            nextNode.next = head
            head = nextNode
            nextNode = next2
            if nextNode == None:
                break
            next2 = nextNode.next
        return head
    
            
