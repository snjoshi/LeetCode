from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t=="":
            return ""
          
        t_count=Counter(t)
        print(t_count)

        s_count=defaultdict(int)
        left=0
        current_count=0
        target_count=len(t_count)
        res=float("inf")
        ans=[-1,-1]
        for right in range(len(s)):
            val=s[right]
            s_count[val]+=1

            if val in t_count and t_count[val]==s_count[val]:
                current_count+=1

            while current_count==target_count:
                if (right -left + 1)<res:
                    res=right -left + 1
                    ans=[left,right]

                s_count[s[left]]-=1
                if s[left] in t_count and t_count[s[left]]>s_count[s[left]]:
                    current_count-=1

                left+=1

        l,r=ans
        if res !=float("inf"):
           return s[l:r+1]
        else:
            return ""



