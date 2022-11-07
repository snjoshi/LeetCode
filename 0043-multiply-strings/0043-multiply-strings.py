class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        
        num1=num1[::-1]
        num2=num2[::-1]
        output=[0]*(len(num1)+len(num2))
       
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul=int(num1[i])*int(num2[j])
                output[i+j]+=mul
                output[i+j+1]+=(output[i+j]//10)
                output[i+j]=output[i+j]%10
                
            
        output = output[::-1]
        lens=0
        while lens<len(output) and output[lens]==0:
            lens+=1
            
        output=map(str,output[lens:])
        return "".join(output)