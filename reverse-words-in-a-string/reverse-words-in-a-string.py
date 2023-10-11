class Solution:
    def reverseWords(self, s: str) -> str:
        left=0
        
        s=s.split()
        print(s)
        
        for i in range(len(s)):
            if s[i]==" ":
                s.remove(s[i])
        right=len(s)-1
        
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
            
        return " ".join(s)
                
        