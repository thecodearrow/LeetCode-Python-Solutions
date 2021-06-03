#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        maxH=0
        maxW=0
        MOD=10**9+7
        for i in range(len(horizontalCuts)-1):
            maxH=max(maxH,horizontalCuts[i+1]-horizontalCuts[i])
        
        for i in range(len(verticalCuts)-1):
            maxW=max(maxW,verticalCuts[i+1]-verticalCuts[i])
        
        return (maxH%MOD*maxW%MOD)%MOD #note! 
            