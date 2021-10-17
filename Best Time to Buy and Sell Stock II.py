class Solution:
   
    def getProfitDP(self,i,canBuy,n,prices,dp):
        #Approach1 
        #DP Solution! 
        if(i>=n):
            return 0
        
        key=(i,canBuy)
        if(key in dp):
            return dp[key]
        if(canBuy):
            #buy
            choice1=-prices[i]+self.getProfitDP(i+1,False,n,prices,dp)
        else:
            #sell
            choice1=prices[i]+self.getProfitDP(i+1,True,n,prices,dp)
        
        #do nothing/hold
        choice2=self.getProfitDP(i+1,canBuy,n,prices,dp)
        dp[key]=max(choice1,choice2)
        return dp[key]
        
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if(n==1):
            return 0
        
        #Approach 2 optimal (greedy)
        total_profit=0
        for i in range(1,n):
            profit=prices[i]-prices[i-1]
            total_profit+=max(0,profit)
        
        #return self.getProfitDP(0,True,n,prices,{})
        return total_profit
        
        
