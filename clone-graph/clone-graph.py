"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1={}

        def dfs(node):
            if node in dict1:
                return dict1[node]

            newNode = Node(node.val)
            dict1[node]=newNode
            for i in node.neighbors:
                newNode.neighbors.append(dfs(i))

            return newNode

        return dfs(node) if node else None
        