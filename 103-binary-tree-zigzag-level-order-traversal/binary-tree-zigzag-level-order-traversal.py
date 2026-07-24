# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        flag=True
        if root is None:
            return []
        queue=deque([root])
        while queue:
            least=[]
            
            for i in range(len(queue)):
                root=queue.popleft()
                least.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if not flag:
                least.reverse()
            
            ans.append(least)
            flag =not flag

        return ans
        