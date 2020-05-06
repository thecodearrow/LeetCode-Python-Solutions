#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        output=[1]*n
        p=1
        for i in range(1,n):
            p*=nums[i-1]
            output[i]=p
        p=1
        for i in range(n-2,-1,-1):
            p*=nums[i+1]
            output[i]=output[i]*p
        
        
        return output
            