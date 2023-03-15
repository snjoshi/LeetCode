class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        preSum=[]
        
        nums.sort()
        print(nums)

        total=0
        for i in nums:
            total=total+i
            preSum.append(total)
            
        print(preSum)
        
        ans=[]
        
        left=0
        right=len(preSum)-1
        for target in queries:
            mid=bisect.bisect_right(preSum,target)
            ans.append(mid)
            
        
        return ans
                
            
        
        