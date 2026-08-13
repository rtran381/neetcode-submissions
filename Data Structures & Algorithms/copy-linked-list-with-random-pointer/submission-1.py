"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = dict()
        copy = head
        while copy:
            c = Node(copy.val)
            hashmap[copy] = c
            copy = copy.next

        second = head
        while second:
            copy = hashmap[second]
            if second.random:
                copy.random = hashmap[second.random]
            else:
                copy.random = None
            if second.next:
                copy.next = hashmap[second.next]
            else:
                copy.next = None
            second = second.next
        if head:
            return hashmap[head]
        return None