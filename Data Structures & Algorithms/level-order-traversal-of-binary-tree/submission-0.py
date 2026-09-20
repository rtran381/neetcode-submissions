# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        level = 0
        cur = []
        cur.append(root)
        while cur:
            ret.append([])
            for i in range(len(cur)):
                node = cur.pop(0)
                ret[level].append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            level += 1
        return ret
