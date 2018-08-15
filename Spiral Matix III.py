#https://leetcode.com/contest/weekly-contest-97/problems/spiral-matrix-iii/

#we walk 1 unit east, then 1 unit south, then 2 units west, then 2 units north, then 3 units east, etc. 


class Solution:
    
    def moveRight(self,pos,R,C,ans):
        i=pos[0]
        j=pos[1]
        j+=1
        pos=[i,j]
        self.update(pos,R,C,ans)
        return pos
    def moveDown(self,pos,R,C,ans):
        i=pos[0]
        j=pos[1]
        i+=1
        pos=[i,j]
        self.update(pos,R,C,ans)
        return pos
    def moveLeft(self,pos,R,C,ans):
        i=pos[0]
        j=pos[1]
        j-=1
        pos=[i,j]
        self.update(pos,R,C,ans)
        return pos
    def moveUp(self,pos,R,C,ans):
        i=pos[0]
        j=pos[1]
        i-=1
        pos=[i,j]
        self.update(pos,R,C,ans)
        return pos
    def update(self,pos,R,C,ans):
        i,j=pos[0],pos[1]
        if(i>=0 and i<R and j>=0 and j<C): #within bounds
            ans.append(pos)


    def spiralMatrixIII(self, R, C, r0, c0):
        ans=[]
        ans.append([r0,c0])
        currentpos=[r0,c0]
        times=0
        while (len(ans)<(R*C)):
            
            
            times+=1 
            for i in range(times):
                currentpos=self.moveRight(currentpos,R,C,ans)
            
            for i in range(times):
                currentpos=self.moveDown(currentpos,R,C,ans)
            
            times+=1
            for i in range(times):
                currentpos=self.moveLeft(currentpos,R,C,ans)
           
            for i in range(times):
                currentpos=self.moveUp(currentpos,R,C,ans)

        return ans
            
