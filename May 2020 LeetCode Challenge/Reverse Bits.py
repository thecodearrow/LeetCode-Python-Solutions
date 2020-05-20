"""
Reverse the bits of an 32 bit unsigned integer A.
"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        pow2=1<<31
        num=A
        reversed=0
        while num:
            if(num&1):
                reversed+=pow2
            pow2>>=1
            num>>=1
        return reversed
