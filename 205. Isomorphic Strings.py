#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st,ts={},{}
        
        for c1,c2 in zip(s,t):
            if((c1 in st.keys() and st[c1]!=c2) or (c2 in ts.keys() and ts[c2]!=c1)):
                return False
            st[c1]=c2
            ts[c2]=c1
        return True

