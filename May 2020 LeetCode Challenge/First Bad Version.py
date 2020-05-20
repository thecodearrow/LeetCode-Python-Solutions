# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        while start<end:
            mid=(start+end)//2
            if(isBadVersion(mid)):
                end=mid
            else:
                start=mid+1
        return start
        
        
        
        