class Solution:
    def myAtoi(self, s: str) -> int:
        s=list(s)
        print(s)
        num=0
        sign=1
        i=0

        while i < len(s) and s[i]==' ':
            i+=1
        
        if i <len(s) and s[i]=="+":
            sign=1
            i+=1
        elif i <len(s) and s[i]=="-":
            sign=-1
            i+=1

        while i < len(s) and s[i].isdigit():
            num = num *10 + int(s[i])

            if sign*num < -2**31:
                return -2**31
            elif sign*num > 2**31 -1:
                return 2**31 -1
            
            i+=1

        return sign*num
        