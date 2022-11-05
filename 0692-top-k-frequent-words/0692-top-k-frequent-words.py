class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashT={}
        Bsort=[[] for i in range(len(words)+1)]
        res=[]
        
        for n in words:
            hashT[n]= 1 + hashT.get(n,0)
        '''    
        for i, j in hashT.items():
            Bsort[j].append(i)
            
        for i in range(len(Bsort)-1,0,-1):
            for n in Bsort[i]:
                res.append(n)
                if len(res)==k:
                    return res
          
        
        for word in words:
            if word in hashT:
                hashT[word]+=1
            else:
                hashT[word]=1
         '''
        heap =[(-i,j) for j,i in hashT.items()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
            