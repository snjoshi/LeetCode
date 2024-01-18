class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1,num2=None, None
        count1,count2=0,0
        ans=[]
        
        for i in nums:  
            if num1==i:
                count1+=1
            elif num2==i:
                count2+=1
            elif count1==0:
                num1=i
                count1+=1
            elif count2==0:
                num2=i
                count2+=1
            else:
                count1-=1
                count2-=1
                
        count1,count2=0,0        
        for i in nums:
            if i==num1:
                count1+=1
            elif i==num2:
                count2+=1
                
        if count1 > len(nums)//3:        
            ans.append(num1)
        if count2 > len(nums)//3:    
            ans.append(num2)
        
        return ans
        
            
        
        