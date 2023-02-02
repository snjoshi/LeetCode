# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#counter to count leaf node
# return min value
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(node, depth):
            if not node:
                return 0
            
            depth_left=findDepth(node.left, depth+1)
            depth_right=findDepth(node.right, depth+1)
            
            if node.left is None and node.right is None:
                return depth
            
            
            if depth_left and depth_right:
                return min(depth_left,depth_right)
            
            return depth_left or depth_right
        
        return findDepth(root,1)
        
        
          
        
         