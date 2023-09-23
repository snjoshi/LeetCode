from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        columns=len(maze[0])

        startR,startC=entrance
        queue=deque()
        queue.append([startR,startC,0])

        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        maze[startR][startC]="+"

        def valid(nextR,nextC):
            if 0<=nextR<rows and 0<=nextC<columns and maze[nextR][nextC]==".":
                return True
            return False

        while queue:
            cRow,cCol,dist=queue.popleft()

            for dx,dy in dirs:
                nextR=cRow+dx
                nextC=cCol+dy

                if valid(nextR,nextC):
                    if nextR==0 or nextR==rows-1 or nextC==0 or nextC==columns-1:
                        return dist+1
                    
                    maze[nextR][nextC]="+"
                    queue.append([nextR,nextC,dist+1])

        return -1
                
        
        
        