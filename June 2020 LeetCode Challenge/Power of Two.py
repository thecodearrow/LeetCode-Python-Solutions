#Given an integer, write a function to determine if it is a power of two.
#https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        is_zero=n&(n-1) == 0
        #For a power of two n&(n-1) would be zero
        return n>0 and is_zero
        