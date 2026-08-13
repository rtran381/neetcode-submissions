# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            if list2 == None:
                return list1
            if list1 == None:
                return list2

            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            
            temp = head

            while list1 and list2:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            
            temp.next = list1 or list2

            return head

        if not lists:
            return ListNode(val='')
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])
        return lists[len(lists)-1]   