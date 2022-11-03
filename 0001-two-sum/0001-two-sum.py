class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        dictn={}
        for i in range(len(nums)):
            dictn[nums[i]]=i
        
        for j in range(len(nums)):
            rem=target - nums[j]
            if rem in dictn.keys() and not dictn[rem]==j:
                ans.append(j)
                ans.append(dictn[rem])
                return ans
                
        
                
                