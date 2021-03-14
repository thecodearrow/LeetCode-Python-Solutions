#https://leetcode.com/problems/set-mismatch/

#Clever Solution based on xor bucketing! 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        #Note xor values should be init to 0 and not 1 
        xor=0
        xor1=0
        xor0=0
        
        
        for i in range(1,n+1):
            xor^=i
        
        for ele in nums:
            xor^=ele
        
        
        diff_bit=xor & ~(xor-1)
        
        for i in range(1,n+1):
            if(i&diff_bit):
                xor1^=i
            else:
                xor0^=i
        
        for ele in nums: 
            if(ele&diff_bit):
                xor1^=ele
            else:
                xor0^=ele
        
        
        for ele in nums:
            if(ele==xor1):
                return [xor1,xor0]
        
        return [xor0,xor1]