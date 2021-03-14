#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected=n*(n+1)//2
        current=sum(nums)
        return expected-current



#Using XOR

#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        missing=0
        for i in range(1,n+1):
            missing^=i
        
        for ele in nums:
            missing^=ele
        
        return missing