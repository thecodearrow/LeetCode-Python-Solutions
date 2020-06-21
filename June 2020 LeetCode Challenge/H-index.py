#https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, A: List[int]) -> int:
        A=sorted(A,reverse=True)
        n=len(A)
        start=1
        end=n
        h=0
        while start<=end:
            mid=(start+end)//2
            if(A[mid-1]>=mid):
                h=mid
                start=mid+1
            else:
                end=mid-1
        
        return h