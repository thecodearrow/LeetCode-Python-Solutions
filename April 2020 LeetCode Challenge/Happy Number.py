#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution(object):
    def getSquareSum(self,n):
        s=0
        while n:
            digit=n%10
            s+=(digit*digit)
            n/=10
        return s
            
            
            
    def isHappy(self, n):
        number=n
        seen_sums={}
        while True:
            if(number==1):
                return True
            if(number in seen_sums):
                return False
            seen_sums[number]=True
            number=self.getSquareSum(number)
            
            
        
    
        
        