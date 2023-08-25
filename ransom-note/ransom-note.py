from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Countr=defaultdict(int)
        Countm=defaultdict(int)
        
        for i in ransomNote:
            Countr[i]+=1
            
        for i in magazine:
            Countm[i]+=1
            
        for key,val in Countr.items():
            if Countm[key]<val or key not in Countr:
                return False
        return True
