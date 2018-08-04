#https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
    	k=k%len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]