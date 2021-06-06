#https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return 0
        if(n==2):
            return abs(nums[1]-nums[0])
        
        nums=sorted(nums)
        moves=0
        
        minEle=nums[0] #at every step you try to get minEle to maxEle
                       #after a step, the secondMaxEle will become the newMaxEle
                     
        for i in range(1,n):
            moves+=nums[i]-small
        
        return moves
            