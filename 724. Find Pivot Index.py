#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        total=sum(nums)
                
        for i in range(len(nums)):
            total=total-nums[i]
            if(total==left):
                return i
            left=left+nums[i]
        return -1

