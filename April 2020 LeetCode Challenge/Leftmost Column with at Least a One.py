#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """s
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m=binaryMatrix.dimensions()
        ans=float("inf")
        down=0
        left=m-1
        while down<n and left>=0:
            i,j=down,left
            cell=binaryMatrix.get(i,j)
            if(cell==1):
                #go left
                ans=min(ans,left)
                left-=1
            else:
                #go down
                down+=1
        if(ans==float("inf")):       
            return -1
        return ans