# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1=[]
        r2=[]
        def fun(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val==q.val:
                r1=fun(p.left,q.left)
                r2=fun(p.right,q.right)
                return r1 and r2
            return False
        return fun(p,q)
