class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*(len(nums))
        
        #prefix
        pre=1
        for i in range(len(nums)):
            output[i]=pre
            pre=pre*nums[i]
            
        #postfix
        post=1
        #output[len(nums)-1]=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=post
            post=post*nums[i]
            
        print(output)
        return output
            
            
        