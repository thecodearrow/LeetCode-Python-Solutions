#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg=True
        if(x>=0):
            neg=False
            
        num=abs(x)
        reversed=str(num)[::-1]
        reversed=int(reversed)
        if(neg):
            reversed=reversed*-1
        l=-2**31
        r=2**31-1
        if(reversed<l or reversed>r):
            reversed=0
        return reversed
        