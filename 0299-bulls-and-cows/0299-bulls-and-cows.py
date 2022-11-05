class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secHash={}
        bulls,cows=0,0
        count={}
        for i in range(len(secret)):    
            secHash[secret[i]]=1+secHash.get(secret[i],0)
                        
        for j in range(len(guess)):
            if guess[j] in secHash and secHash[guess[j]]>0 and guess[j]==secret[j]:
                bulls+=1
                secHash[guess[j]]-=1
            
        for j in range(len(guess)):
            if guess[j] in secHash and secHash[guess[j]]>0 and guess[j]!=secret[j]:
                cows+=1
                secHash[guess[j]]-=1
                
        ans=str(bulls)+"A"+str(cows)+"B"
        
        return ans
                
                