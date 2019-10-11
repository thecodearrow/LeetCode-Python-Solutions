#https://leetcode.com/problems/path-with-maximum-gold/submissions/

class Solution(object):
    def __init__(self):
        self.bestSum=0
    def isValid(self,i,j,n,c,grid):
        if(i>=0 and j>=0):
            if(i<n and j<c):
                if(grid[i][j]):
                    return True
            
        return False
    def bestSumFromNode(self,i,j,n,c,currentSum,grid,visited):
        currentSum+=grid[i][j]
        visited[i][j]=True
        neighbours=[[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
        noPath=True
        for x,y in neighbours:
            if(self.isValid(x,y,n,c,grid)):
                if(not visited[x][y]):
                    self.bestSumFromNode(x,y,n,c,currentSum,grid,visited)
                    
        self.bestSum=max(currentSum,self.bestSum)
        visited[i][j]=False
    
    def resetVisited(self,n,c):
        return [[False for i in range(c)]for j in range(n)]
    def getMaximumGold(self, grid):
        n=len(grid)
        c=len(grid[0])
        for i in range(n):
            for j in range(c):
                if(grid[i][j]):
                    visited=self.resetVisited(n,c)
                    self.bestSumFromNode(i,j,n,c,0,grid,visited)
                    
                
        return self.bestSum
        
        

        
        