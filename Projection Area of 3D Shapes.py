#https://leetcode.com/contest/weekly-contest-96/problems/projection-area-of-3d-shapes/


class Solution:
    def projectionArea(self, grid):
       
        
        #top view = count of all non zero height blocks
        
        top=0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if(grid[i][j]>0):
                    top+=1
                
        front=[0]*(len(grid[0])) #max height of col =frontview
        side=[] #max height of row = side view
        
        for i in range(len(grid)):
            side.append(max(grid[i]))  #row wise
            
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                front[j]=max(front[j],grid[i][j])
                
        
        ans=top+sum(front)+sum(side)
        return ans
            
        