# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.sumT=0
        def maxDepth(node):
            if not node:
                return 0
            
            left=maxDepth(node.left)
            right=maxDepth(node.right)
            
            return max(left,right)+1
                
        def dfs(node,depth,Mdepth):
            if not node:
                return 0
            
            if node.right is None and node.left is None and depth==Mdepth:
                self.sumT+=node.val
                
            dfs(node.left,depth+1,Mdepth)
            dfs(node.right,depth+1,Mdepth)
                
            
        Mdepth = maxDepth(root)
        print(Mdepth)
        dfs(root,1,Mdepth)
        return self.sumT
        
        