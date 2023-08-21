from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=defaultdict(int)
        losers=defaultdict(int)
        
        final_winner=set()
        final_loser=set()
        
        for i in range(len(matches)):
            winners[matches[i][0]]+=1
            losers[matches[i][1]]+=1
            
        
        for i in winners.keys():
            print(i)
            if i not in losers:
                final_winner.add(i)
                
        for i in losers.keys():
            if losers[i]==1:
                final_loser.add(i)
                
        return [sorted(list(final_winner)),sorted(list(final_loser))]