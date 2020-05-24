#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans=0
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]):
                    if(i>0 and j>0):
                        matrix[i][j]=min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
                    ans+=matrix[i][j]
        
        return ans
        