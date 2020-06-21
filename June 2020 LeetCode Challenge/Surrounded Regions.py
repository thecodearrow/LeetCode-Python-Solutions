#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3363/

class Solution:
    def dfs(self,board,i,j,n,m):
        if(i>=0 and j>=0 and i<n and j<m):
            if(board[i][j]=="O"):
                board[i][j]="#"
                board=self.dfs(board,i+1,j,n,m)
                board=self.dfs(board,i-1,j,n,m)
                board=self.dfs(board,i,j+1,n,m)
                board=self.dfs(board,i,j-1,n,m)
        
        return board
    def updateBoundaryConnected(self,board,n,m):
        #top row
        for j in range(m):
            if(board[0][j]=="O"):
                board=self.dfs(board,0,j,n,m)
        #bottom row
        for j in range(m):
            if(board[n-1][j]=="O"):
                board=self.dfs(board,n-1,j,n,m)
        #left column
        for i in range(n):
            if(board[i][0]=="O"):
                board=self.dfs(board,i,0,n,m)
    
        #right column
        for i in range(n):
            if(board[i][m-1]=="O"):
                board=self.dfs(board,i,m-1,n,m)
        return board
        
           
    def solve(self, board: List[List[str]],i=0,j=0) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if(len(board)==0):
            return 
        visited=defaultdict(lambda:False)
        n=len(board)
        m=len(board[0])
        board=self.updateBoundaryConnected(board,n,m)
        
        for i in range(n):
            for j in range(m):
                if(board[i][j]=="O"):
                    board[i][j]="X"
                elif(board[i][j]=="#"):
                    board[i][j]="O" #revert back