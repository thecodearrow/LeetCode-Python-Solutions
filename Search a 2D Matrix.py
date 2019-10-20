#https://leetcode.com/problems/search-a-2d-matrix/submissions/
class Solution:
    def findColPosition(self,row_pos,a,x,m):
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            if(a[row_pos][mid]==x):
                return True
            elif(a[row_pos][mid]<x):
                low=mid+1
            else:
                high=mid-1
        return False
    def findRowPosition(self,a,x,n):
        low=0
        high=n-1
        while low<high:
            mid=(low+high+1)//2
            if(a[mid][0]>x):
                high=mid-1
            else:
                low=mid
        return low
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N=len(matrix)
        if(N==0):
            return False
        M=len(matrix[0])
        if(M==0):
            return False
        row_pos=self.findRowPosition(matrix,target,N)
        if(matrix[row_pos][0]==target):
            return True
        col_pos=self.findColPosition(row_pos,matrix,target,M)
        if(col_pos):
            return True
        return False