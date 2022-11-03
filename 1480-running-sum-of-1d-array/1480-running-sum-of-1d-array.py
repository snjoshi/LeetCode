class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p = []
        k=0
        i=len(nums)
        for i in nums:
            k=k+i
            p.append(k)
        return p