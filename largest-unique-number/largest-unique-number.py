from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count=defaultdict(int)
        ans=[]
        
        for i in nums:
            count[i]+=1
        
        for k,v in count.items():
            if v==1:
                ans.append(k)
                
        return max(ans,default=-1)
                
        
        