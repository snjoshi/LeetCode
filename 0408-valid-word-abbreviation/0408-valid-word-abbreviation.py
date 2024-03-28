class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0
        num=""
        while i<len(word) and j<len(abbr):
            if abbr[j].isalpha():
                if abbr[j]!=word[i]:
                    return False
                j+=1
                i+=1   
            else:
                while j<len(abbr) and abbr[j].isnumeric():
                    num+=abbr[j]
                    j+=1
                if num[0]=="0":
                    return False
                jump=int(num)
                i+=jump
                num=""

        return i == len(word) and j == len(abbr)
