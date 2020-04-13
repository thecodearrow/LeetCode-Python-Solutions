#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution(object):
    def maxProfit(self, prices):
        if(len(prices)==0):
            return 0
        ans=0
        for i in range(1,len(prices)):
            profit=prices[i]-prices[i-1]
            if(profit>0):
                ans+=profit
                
        return ans