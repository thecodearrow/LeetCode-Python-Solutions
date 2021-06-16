#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3780/

class Solution:
    def isPossible(self,i,sums,ideal_side,n,matchsticks):
        #O(4^n)
        if(i==n):
            side1,side2,side3,side4=sums
            if(side1==side2==side3==side4==ideal_side):
                return True
            return False
        
        for j in range(4):
            sums[j]+=matchsticks[i]
            if(sums[j]<=ideal_side):
                if(self.isPossible(i+1,sums,ideal_side,n,matchsticks)):
                    return True
            sums[j]-=matchsticks[i]
                
        
        return False
    
        
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        perimeter=sum(matchsticks)
        ideal_side=perimeter//4
        if(perimeter%4!=0):
            return False
        matchsticks=sorted(matchsticks,reverse=True) #Sorting by reverse helps prevent TLE (NOTE!)
        status=self.isPossible(0,[0,0,0,0],ideal_side,n,matchsticks)
        return status
        