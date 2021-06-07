#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums) #set of seen elements! 
        maxL=0
        traversed=set() #handles edge case when nums=[1,2,3,4,1,1,1,1,1,1]
        for ele in nums:
            if(ele-1 not in seen):
                l=0
                #go right as much as possible! 
                curr=ele
                while curr in seen and curr not in traversed:
                    traversed.add(curr)
                    curr+=1
                    l+=1
                maxL=max(l,maxL)
            
        
        return maxL
                    
                
        