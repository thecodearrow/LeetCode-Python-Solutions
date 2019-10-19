#https://leetcode.com/problems/longest-consecutive-sequence/submissions/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        longest_streak=1
        present=set(nums)
        for ele in nums:
            if((ele-1) not in present):
                #Try building a streak from here!
                start=ele
                l=0
                while start in present:
                    l+=1
                    start+=1
                longest_streak=max(longest_streak,l)
                    
                
        return longest_streak
        
        