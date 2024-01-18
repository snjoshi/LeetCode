class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #n*(n+1)/2 - sum(num)
        return len(nums)*(len(nums)+1)//2 - sum(nums)
