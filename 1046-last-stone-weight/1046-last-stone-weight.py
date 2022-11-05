class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            y=stones[0]
            x=stones[1]
            
            if(x==y):
                stones.remove(x)
                stones.remove(y)
            else:
                new=0
                new=y-x
                stones.remove(x)
                stones.remove(y)
                stones.append(new)
        
        stones.append(0)
       
        return stones[0]
        
        