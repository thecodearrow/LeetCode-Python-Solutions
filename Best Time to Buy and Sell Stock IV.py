class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if(2*k>=len(prices)):
            #SPECIAL CASE! we can do as many trades as we want! 
            #Note— The recursion takes care of this, so this is only an optimisation! 
            ans=0
            for i in range(1,len(prices)):
                p=prices[i]-prices[i-1]
                ans+=max(p,0)
            return ans
                
        def getMaxProfit(i,k,canBuy,dp):
            if(i==len(prices)):
                return 0
            if(k==0):
                return 0
            key=(i,k,canBuy)
            if(key in dp):
                return dp[key]
            
            if(canBuy):
                choice1=-prices[i]+getMaxProfit(i+1,k,False,dp) #buy
                choice2=getMaxProfit(i+1,k,True,dp) #not buy
            else:
                choice1=prices[i]+getMaxProfit(i+1,k-1,True,dp)
                choice2=getMaxProfit(i+1,k,False,dp)
            dp[key]=max(choice1,choice2)
            return dp[key]
                
        return getMaxProfit(0,k,True,{})
