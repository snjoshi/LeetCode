#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        i=0
        
        while i<len(t) and k<len(s):
            if(t[i]==s[k]):
                k=k+1
            i=i+1
        if(k==len(s)):
            return True
        else:
            return False
        

