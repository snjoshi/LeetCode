from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        
        for i in range(len(strs)):
            dict1[tuple(sorted(strs[i]))].append(strs[i])
            
                
        return dict1.values()
        
        
        