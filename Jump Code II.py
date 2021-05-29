#https://leetcode.com/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<=1):
            return 0

        curr=nums[0]
        maxJump=curr
        jumps=1
        for i in range(1,n):
            if(i==n-1):
                #reached end! 
                return jumps
            maxJump=max(maxJump,i+nums[i])
            curr-=1
            if(curr==0):
                if(maxJump==0):
                    #can't make it!
                    return -1
                jumps+=1
                curr=maxJump-i
            
            
            
        
        return -1 #not possible