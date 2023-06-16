# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.result=0

        def dfs(node, curr_min, curr_max):
            if not node:
                return
            
            self.result=max(self.result, abs(curr_max - node.val), abs(curr_min - node.val))
            curr_min=min(node.val, curr_min)
            curr_max=max(node.val, curr_max)

            dfs(node.left,curr_min, curr_max)
            dfs(node.right,curr_min, curr_max)

            return self.result
        
        dfs(root,root.val,root.val)

        return self.result