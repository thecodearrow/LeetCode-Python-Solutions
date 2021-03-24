#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/

class Solution:
    
    def reorderedPowerOf2(self, N: int) -> bool:
        def digitsArray(n):
            dig=[0]*10
            while n:
                d=n%10
                dig[d]+=1
                n//=10

            return dig
            
        pow2=1
        digitsArrayN=digitsArray(N)
        for i in range(32):
            if(digitsArray(pow2)==digitsArrayN):
                return True
            pow2<<=1
        
        return False
            