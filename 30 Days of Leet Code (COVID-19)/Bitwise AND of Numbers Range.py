#https://leetcode.com/problems/bitwise-and-of-numbers-range/

#https://www.youtube.com/watch?v=tM-FPbMh-SQ&t=191s

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        iterations=0
        while m!=n:
            iterations+=1
            m>>=1
            n>>=1
        
        ans=m
        while iterations!=0:
            iterations-=1
            ans<<=1
            
        
        return ans    
        
            
        