#https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)
     
        