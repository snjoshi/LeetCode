class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        sliding_set=set()
        left=0
        count=0
        
        for i in s:
            while i in sliding_set:
                sliding_set.remove(s[left])
                left+=1
                
            sliding_set.add(i)
            count=max(count,len(sliding_set))
            
            
        return count
    
    
        