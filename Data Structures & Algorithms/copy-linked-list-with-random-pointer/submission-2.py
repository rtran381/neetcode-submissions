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
        if head is None:
            return None
        hashmap = {None: None}
        
        copy = head
        while copy:
            c = Node(copy.val)
            hashmap[copy] = c
            copy = copy.next

        second = head
        while second:
            copy = hashmap[second]
            copy.random = hashmap[second.random]
            copy.next = hashmap[second.next]
            second = second.next
        return hashmap[head]