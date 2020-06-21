"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for c in coins:
            for i in range(1,amount+1):
                if(c<=i):
                    dp[i]+=dp[i-c]
                
        return dp[amount]
        