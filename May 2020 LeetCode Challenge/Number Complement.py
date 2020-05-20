#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
class Solution:
    def findComplement(self, num: int) -> int:
        complement=0
        pow2=1
        while num:
            bit=num&1
            if(bit==0):
                complement+=pow2
            pow2*=2
            num>>=1
        return complement
        