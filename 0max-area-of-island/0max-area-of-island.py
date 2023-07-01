class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        seen=set()

        ans=0
        row = len(grid)
        col=len(grid[0])
        #print(row,col)
        maxA=0

        def dfs(i,j):
            nonlocal ans,maxA
            for x,y in direc:
                maxA=max(ans,maxA)
                m=i+x
                n=j+y
                if m>=0 and n>=0 and m<row and n<col and grid[m][n]==1 and (m,n) not in seen:
                    ans+=1
                    seen.add((m,n))
                    dfs(m,n)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in seen:
                    seen.add((i,j))
                    
                    ans=1
                    dfs(i,j)

        return maxA