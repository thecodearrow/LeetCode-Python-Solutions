"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""
class Solution:         
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if(n==0):
            return []
        nums=sorted(nums)
        lds=[1]*n
        parent=[None]*n
        max_length=0
        max_idx=0
        for i in range(1,n):
            for j in range(i):
                if(nums[i]%nums[j]==0):
                    if(lds[j]+1>lds[i]):
                        lds[i]=lds[j]+1
                        parent[i]=j
                    if(lds[i]>max_length):
                        max_length=lds[i]
                        max_idx=i
        
        current_idx=max_idx
        subset=[]
        while current_idx!=None:
            subset.append(nums[current_idx])
            current_idx=parent[current_idx]
            
        return subset
            
                        
        
                    
        
                    
            
            
       
        
            