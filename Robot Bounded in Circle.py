class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs=[(-1,0),(0,1),(1,0),(0,-1)] #dirs N,R,S,L
        d=0
        x,y=0,0
        for i in range(4):
            #one iteration
            for c in instructions:
                if(c=='G'):
                    dx,dy=dirs[d]
                    x+=dx
                    y+=dy
                elif(c=='L'):
                    d=(d-1)%4
                elif(c=='R'):
                    d=(d+1)%4
        
        
        return x==0 and y==0 #after 4 cycles back to (0,0)
                
