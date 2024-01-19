"""
1 1 1 1 0 0 0 0 
1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        seen=set()
        if not grid:
            return 0

        rows,columns=len(grid),len(grid[0])

        def bfs(r,c):
            queue=collections.deque()
            seen.add((r,c))
            queue.append((r,c))

            while queue:
                i,j=queue.popleft()
                direction=[[1,0],[0,1],[-1,0],[0,-1]]
                for x,y in direction:
                    row,col=i+x,y+j
                    if(0<=row<rows and 0<=col<columns and (row,col) not in seen and grid[row][col]=="1"):

                        queue.append((row,col))
                        seen.add((row,col))


        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r,c)
                    ans+=1


        return ans