class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverseString(left,right):
            while left < right:
                temp=s[left]
                s[left]=s[right]
                s[right]=temp
                left+=1
                right-=1

           # print(s)
            
        def reverseWord():
            left=0
            last=0
            n=len(s)
            while left<n:
                while last<n and s[last]!=" ":
                    last+=1
                    
                reverseString(left,last-1)
                
                left=last+1
                last+=1
        
        left=0
        right=len(s)-1
        reverseString(left,right)

        reverseWord()
