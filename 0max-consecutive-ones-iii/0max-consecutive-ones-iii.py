class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #1,1,1,0,0,0,1,1,1,1,0
        
        left,right=0,0
        count=0
        size=0
        
        for right in range(len(nums)):
            if nums[right]==0 and count>=k:
                while nums[left]!=0:
                    left+=1
                #count-=1
                left+=1
                
            elif nums[right]==0 and count<k:
                count+=1
            
            print("left:",left)
            print("right:",right)
            print("count:",count)
            
            size = max(size,right-left+1)
            print(size)
            
        return size
            
                
                