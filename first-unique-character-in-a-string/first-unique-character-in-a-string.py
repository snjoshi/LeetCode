from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict2=Counter(s)
        print(dict2)
        
        for i in range(len(s)):
            if s[i] in dict2 and dict2[s[i]]==1:
                return i
            
        return -1
        
        