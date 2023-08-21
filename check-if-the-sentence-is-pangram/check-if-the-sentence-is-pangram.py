class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pan=set()
        
        for i in range(0,len(sentence)):
            if sentence[i] not in pan:
                pan.add(sentence[i])
                
        
        if len(pan)==26:
            return True
        return False