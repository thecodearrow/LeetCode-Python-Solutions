#https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3285/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        current_sum=nums[0]
        for i in range(1,len(nums)):
            current_sum=max(current_sum+nums[i],nums[i])
            max_sum=max(current_sum,max_sum)
        return max_sum
            
        