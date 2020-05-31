"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""
#Think about what shifting right does! 
class Solution:
    def setBits(self,n):
        count=0
        while n:
            count+=1
            n=n&(n-1) #unset the last set bit
        return count
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            dp[i]=dp[i//2]
            if(i%2!=0):
                dp[i]+=1
        return dp