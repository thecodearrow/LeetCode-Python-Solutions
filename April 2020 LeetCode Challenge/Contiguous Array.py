#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        seen={}
        seen[0]=-1
        count=0
        for i in range(n):
            ele=nums[i]
            if(ele==1):
                count+=1
            else:
                count-=1
            if(count in seen):
                current_length=i-seen[count]
                ans=max(ans,current_length)      
            else:
                seen[count]=i
            
        return ans
                