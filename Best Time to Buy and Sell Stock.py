#Divide and Conquer Strategy (O(NLogN) )

class Solution:
    def getMax(self,i,j,prices):
        return max(prices[i:j+1])
    def getMin(self,i,j,prices):
        return min(prices[i:j+1])
    def divideandconquer(self,low,high,prices):
        if(low>=high):
            return 0
        mid=(low+high)//2
        left=self.divideandconquer(low,mid,prices) #get the transaction from left subarray
        right=self.divideandconquer(mid+1,high,prices) #get the transaction from right subarray
        both=self.getMax(mid+1,high,prices)-self.getMin(low,mid,prices) #buy min price from left and sell max price from right
        return max(both,left,right)
    def maxProfit(self, prices: List[int]) -> int:
        #Let's use Divide and Conquer Strategy
        n=len(prices)
        return self.divideandconquer(0,n-1,prices)
      

      
#O(N) Approach! 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestMin=prices[0]
        n=len(prices)
        maxProfit=0 #no transactions
        for i in range(1,n):
            profit=prices[i]-bestMin
            maxProfit=max(maxProfit,profit)
            bestMin=min(prices[i],bestMin)
        
        return maxProfit
        
