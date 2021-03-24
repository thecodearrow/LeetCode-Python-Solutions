#https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return nums[0]
        nums=sorted(nums)
        print(nums)
        if(nums[0]!=nums[1]):
            return nums[0]
        if(nums[n-1]!=nums[n-2]):
            return nums[n-1]
        for i in range(1,n-1):
            if((nums[i]!=nums[i-1] and nums[i]!=nums[i+1])):
                return nums[i]
        