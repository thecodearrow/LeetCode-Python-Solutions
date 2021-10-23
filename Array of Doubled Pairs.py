#Similar to https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr=sorted(arr,key=abs) #needs sorting by absolute values for it work
        count=Counter(arr)
        for ele in arr:
            if(count[ele]==0):
                #already mapped
                continue
            if(count[2*ele]==0):
                return False
            count[ele]-=1
            count[2*ele]-=1
            
            
        
        return True
