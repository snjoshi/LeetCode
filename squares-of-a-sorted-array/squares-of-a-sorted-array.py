class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        left=0
        right=len(nums)-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                ans.insert(0,nums[left]**2)
                left+=1
            else:
                ans.insert(0,nums[right]**2)
                right-=1

        return ans
        