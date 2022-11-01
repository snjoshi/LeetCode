class Solution:
    def climbStairs(self, n: int) -> int:
        
        i=1
        j=1
        
        for k in range(n-1):
            temp=i
            i=i+j
            j=temp
            
        return i
        