#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3310/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if(n<=1):
            return True
        steps=nums[0]
        maxReach=0
        for i in range(n):
            if(i==n-1):
                return True
            maxReach=max(maxReach,nums[i]+i)
            if(steps==0):
                steps=maxReach-i
                if(steps==0):
                    return False
            steps-=1
        
        return True