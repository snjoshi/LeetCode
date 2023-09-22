# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
start: root
max abs of a and b
'''
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diff = 0

        def dfs(node, cmax, cmin):
            if not node:
                return

            cmax=max(cmax, node.val)
            cmin=min(cmin,node.val)
            self.diff=max(self.diff, abs(cmax - node.val),abs(cmin -node.val))
            dfs(node.left,cmax, cmin)
            dfs(node.right,cmax, cmin)

        dfs(root, root.val, root.val)

        return self.diff
            

        