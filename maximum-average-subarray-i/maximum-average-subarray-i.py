class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        1,12,-5,-6,50,3
        
        right,left=0,0
        avg=float("-inf")
        total=0
        for right in range(len(nums)):
            if right-left+1 > k:
                total-=nums[left]
                left+=1
                
            total+=nums[right]
            
            if right-left+1==k:
                avg = max(avg,total/k)
            
        return avg
            
            

            
            
            
            
        