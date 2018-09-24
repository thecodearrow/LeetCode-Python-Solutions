

#https://leetcode.com/problems/coin-change/description/
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX_INT=10**9+7
        dp=[]
        coins=sorted(coins)
        for i in range(amount+1):
            dp.append(MAX_INT)
        
        dp[0]=0
        
        for c in coins:
            for amt in range(1,amount+1):
                if(amt-c>=0):
                    dp[amt]=min(dp[amt-c]+1,dp[amt]) 
        
        if(dp[amount]>=MAX_INT):
            return -1
        return dp[amount]
        
