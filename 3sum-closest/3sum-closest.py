class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=float('inf')
        nums.sort()
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1

            while left<right:
                temp = target - (nums[left]+nums[right]+nums[i])
                if abs(temp)<abs(ans):
                    ans=temp
                if (nums[left]+nums[right]+nums[i])<target:
                    left+=1
                else:
                    right-=1
            if ans == 0:
                break
            
        return target - ans
                
