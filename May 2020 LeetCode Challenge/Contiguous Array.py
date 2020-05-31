#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

"""
Replace 0 with -1 and this problem reduces to finding the largest subarray with sum=0
This can be easily found by keeping track of sums we have seen so far. 
If we find the same sum again, that means we found a subarray in between with sum=0
Keep track of all such subarray lengths and return the max out of all of them 
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[i]==0):
                nums[i]=-1 
        
        seen_sum={0:-1} #base case before starting the traversal, the sum was zero! 
                        #sums seen with the index of the fist occurrence
        current_sum=0
        max_length=0
        for i,ele in enumerate(nums):
            current_sum+=ele
            if(current_sum in seen_sum):
                max_length=max(max_length,i-seen_sum[current_sum])
            else:
                seen_sum[current_sum]=i
                    
        
        return max_length