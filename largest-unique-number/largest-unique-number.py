from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count=defaultdict(int)
        ans=-1
        
        for i in nums:
            count[i]+=1
        
        for k,v in count.items():
            if v==1:
                ans=max(k,ans)
                
        return ans
                
        
        