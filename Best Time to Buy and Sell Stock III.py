class Solution:
    def approach2(prices):
        #Approach2— One-pass Simulation
        firstBuy=float("inf") #minimise this! 
        firstProfit=0
        secondBuy=-float("inf") #i want to ensure I have most money in pocket
        secondProfit=0
        for price in prices:
            firstBuy=min(firstBuy,price)
            firstProfit=max(firstProfit,price-firstBuy)
            secondBuy=max(secondBuy,firstProfit-price)
            secondProfit=max(secondProfit,price+secondBuy)
        return secondProfit
    def maxProfit(self, prices: List[int]) -> int:
        #Approach1 - Bidirectional DP
        n=len(prices)
        left_max=[0]*n #profit till i from left
        minBuy=prices[0]
        for i in range(1,n):
            profit=prices[i]-minBuy
            left_max[i]=max(left_max[i-1],profit) 
            minBuy=min(minBuy,prices[i])
        right_max=[0]*n #profit I can make after i
        maxSell=prices[-1]
        for i in range(n-2,-1,-1):
            profit=maxSell-prices[i]
            right_max[i]=max(right_max[i+1],profit)
            maxSell=max(maxSell,prices[i])
        
        ans=0 #max_profit with at most 2 transactions
        for i in range(1,n):
            # one_buy=left_max[i]
            # two_buys=left_max[i-1]+right_max[i]
            # ans=max(one_buy,two_buys,ans)
            buy=left_max[i]+right_max[i]
            ans=max(ans,buy)
        
        return ans
            
                
            
        
