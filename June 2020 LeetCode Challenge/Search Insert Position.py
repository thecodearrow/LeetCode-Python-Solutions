"""
#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        pos=n
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if(target<=nums[mid]):
                if(nums[mid]==target):
                    return mid
                pos=mid
                end=mid-1
            else:
                start=mid+1
        
        return pos
                
            