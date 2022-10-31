#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p = []
        k=0
        i=len(nums)
        for i in nums:
            k=k+i
            p.append(k)
        return pv

