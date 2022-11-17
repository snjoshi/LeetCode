class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        n=len(grid)
        m=len(grid[0])
        dp = [[-2 for x in range(105)] for y in range(105)]
        
        def bounds(i,j):
             return (i>=0 and i<n and j>=0 and j<m)
                
        
        def dfs(grid,i,j):
            if i==n:
                return j
            if bounds(i,j):
                if(grid[i][j]==1 and bounds(i,j+1) and grid[i][j+1]==1):
                    if dp[i+1][j+1] is not -2:
                        return dp[i+1][j+1]
                    else:
                        dp[i+1][j+1]=dfs(grid,i+1,j+1)
                        return dp[i+1][j+1]
                if grid[i][j]==-1 and bounds(i,j-1) and grid[i][j-1]==-1:
                    if dp[i+1][j-1] is not -2:
                        return dp[i+1][j-1]
                    else:
                        dp[i+1][j-1]=dfs(grid,i+1,j-1)
                        return dp[i+1][j-1]
            
            return -1
                    
           
            
        
        
        for i in range(n):
            for j in range(m):
                dp[i][j]=-2
                
        ans=[]
        for i in range(m):
            ans.append(dfs(grid,0,i))
            
        return ans
        