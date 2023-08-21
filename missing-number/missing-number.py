class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        n=len(nums)
        real_total=n*(n+1)/2
        
        return int(real_total - total)
        
        