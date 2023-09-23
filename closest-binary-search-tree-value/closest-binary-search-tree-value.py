# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return 0
        
        minN=float("inf")
        ans=0
        nodes=[]
        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)

        dfs(root)
        print(nodes)
        final=0
        for i in nodes:
            if minN > abs(i-target):
                minN=abs(i-target)
                final = i

        return final
        
                