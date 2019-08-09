#https://leetcode.com/problems/rotate-image/submissions/

import math
class Solution:
    
    def next_rotate(self,i,j,n):
        """Returns the coords after 90 degree rotation"""
        return ((j,n-1-i))

    def rotate(self, matrix: List[List[int]]):
        n=len(matrix[0])
        for i in range(math.ceil(n/2)):
            for j in range(math.floor(n/2)):
                x,y=i,j
                temp=[0,0,0,0]
                for k in range(4):
                    temp[k]=matrix[x][y]
                    x,y=self.next_rotate(x,y,n)
                    
                for k in range(4):
                    matrix[x][y]=temp[(k+3)%4]  #previous cube 
                    x,y=self.next_rotate(x,y,n)
                    
                
                    
                
                
        
        