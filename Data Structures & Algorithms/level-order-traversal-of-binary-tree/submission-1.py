# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        
        cur = []
        cur.append(root)
        while cur:
            level = []
            for i in range(len(cur)):
                node = cur.pop(0)
                if node:
                    level.append(node.val)
                    cur.append(node.left)
                    cur.append(node.right)
            if level:
                ret.append(level)
        return ret
