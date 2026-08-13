class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.l, self.r = Node(0,0), Node(0,0) #dummy nodes for left and right boundaries
        self.l.next, self.r.prev = self.r, self.l

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def insert(self, node): # insert at back
        p, n = self.r.prev, self.r
        p.next, n.prev = node, node
        node.next, node.prev = n, p

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least = self.l.next
            self.remove(least)
            del self.cache[least.key]
            
