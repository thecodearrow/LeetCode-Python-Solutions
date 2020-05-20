#https://leetcode.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/

class Solution:
    def findPivot(self,A):
        last_element=A[-1]
        start=0
        end=len(A)-1
        pivot=None
        while start<=end:
            mid=start+(end-start)//2
            if(A[mid]<=last_element):
                pivot=mid
                end=mid-1
            else:
                start=mid+1
        return pivot
                
    def binarySearch(self,A,start,end,target):
        while start<=end:
            mid=start+(end-start)//2
            if(A[mid]==target):
                return mid
            elif(A[mid]<target):
                start=mid+1
            else:
                end=mid-1
        return -1
    def search(self, A: List[int], target: int) -> int:
        n=len(A)
        if(n==0):
            return -1
        p=self.findPivot(A)
        #0-p-1 will be sorted
        #p to n-1 will be sorted
        last_element=A[-1]
        if(target<=last_element):
            #target will be found in the second half
            return self.binarySearch(A,p,n-1,target)
        else:
            #target will be found in the first half
            return self.binarySearch(A,0,p-1,target)

        
        
        
        