"""
#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

#Moore's Voting Booth Algorithm!
class Solution:
    def verifyMajorityElement(self,majority,a):
        n=len(a)
        count=0
        for ele in a:
            if(ele==majority):
                count+=1
        if(count>(n//2)):
            return True
        return False
            
    def majorityElement(self, nums: List[int]) -> int:
        majority=None
        count=0
        for ele in nums:
            if(majority is None or count==0):
                majority=ele
                count=1
            else:
                if(ele==majority):
                    count+=1
                else:
                    count-=1 
                    
        if(count!=0):
            if(self.verifyMajorityElement(majority,nums)):
                #This check is not needed since it is given that the majority element always exists!
                #However, it is necessary if majority element is not guaranteed to exist!
                return majority
        
        return -1