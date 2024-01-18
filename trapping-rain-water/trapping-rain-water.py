class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[]
        maxRight=[]
        ans=0
        leftval=0
        for i in range(len(height)):
            if height[i]>leftval:
                maxLeft.append(height[i])
                leftval=height[i]
            else:
                maxLeft.append(leftval)
        rightval=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>rightval:
                maxRight.insert(0,height[i])
                rightval=height[i]
            else:
                maxRight.insert(0,rightval)

        print(maxLeft)
        print(maxRight)
            
        for i in range(len(height)):
            val = min(maxLeft[i],maxRight[i])-height[i]
            if val>0:
                ans+=val
            else:
                ans+=0 

        return ans

        
        