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
        q=deque([root] if root else [])

        while q:
            level=[]
            for i in range(len(q)):
                node =q.popleft()
                level.append(node.val)
                if node.left:
                     q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level = reversed(level) if len(ans) % 2 else level
            ans.append(level)

        return ans

                
