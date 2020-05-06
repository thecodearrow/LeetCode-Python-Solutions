#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/

class Solution:
    def findMinPathSum(self,grid,i,j,m,n,cache):
        pos=(i,j)
        if(i==m-1 and j==n-1):
            return grid[i][j]
        if(pos in cache):
            return cache[pos]
        if(i==m-1):
            cache[pos]=grid[i][j]+self.findMinPathSum(grid,i,j+1,m,n,cache)
        elif(j==n-1):
            cache[pos]=grid[i][j]+self.findMinPathSum(grid,i+1,j,m,n,cache) 
        else:
            path1=self.findMinPathSum(grid,i,j+1,m,n,cache)
            path2=self.findMinPathSum(grid,i+1,j,m,n,cache)
            cache[pos]=grid[i][j]+min(path1,path2)
        return cache[pos]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if(m==0):
            return 0
        n=len(grid[0])
        return self.findMinPathSum(grid,0,0,m,n,{})
        