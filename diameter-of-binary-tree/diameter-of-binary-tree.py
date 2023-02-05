# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        diameter=0
        
        def longPath(node):
            nonlocal diameter
            if not node:
                return 0
            
            leftSide=longPath(node.left)
            rightSide=longPath(node.right)
            
            length=leftSide+rightSide
            diameter=max(diameter,length)
            
            return max(leftSide,rightSide)+1
        
        longPath(root)
        return diameter
        