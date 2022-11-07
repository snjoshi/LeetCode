class Solution:
    def isHappy(self, n: int) -> bool:
            visited=set()
            
            def sumOfsq(n):
                sum=0
                while n:
                    dig=n%10
                    dig=dig**2
                    sum+=dig
                    n=n//10
                return sum
            
            
            while n not in visited:
                visited.add(n)
                
                n= sumOfsq(n)
                
                if n==1:
                    return True
            return False
            
         