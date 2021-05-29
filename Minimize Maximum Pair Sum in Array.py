#https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        ans=0
        while i<j:
            ans=max(ans,nums[i]+nums[j])
            i+=1
            j-=1
        
        return ans
        