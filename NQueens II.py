#https://leetcode.com/problems/n-queens-ii/submissions/

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def isValid(i,j):
            #in O(1)
            global rowSet,colSet,diag1Set,diag2Set,board
            if(i not in rowSet):
                if(j not in colSet):
                    if((i+j) not in diag1Set):
                        if((i-j) not in diag2Set):
                            return True
            return False
        def markPosition(i,j):
            global rowSet,colSet,diag1Set,diag2Set,board
            board[i][j]='Q'
            rowSet.add(i)
            colSet.add(j)
            diag1Set.add(i+j)
            diag2Set.add(i-j)
        
        def unMarkPosition(i,j):
            global rowSet,colSet,diag1Set,diag2Set,board
            board[i][j]='.'
            rowSet.remove(i)
            colSet.remove(j)
            diag1Set.remove(i+j)
            diag2Set.remove(i-j)
            
        def getNQueens(i,n):
            if(i==n):
                global ans
                ans+=1
                return
            
            global board
            for j in range(n):
                if(isValid(i,j)):
                    markPosition(i,j)
                    getNQueens(i+1,n)
                    unMarkPosition(i,j)
                
            
       
        global ans,board,rowSet,colSet,diag1Set,diag2Set
        board=[["." for j in range(n)] for i in range(n)]
        rowSet,colSet,diag1Set,diag2Set=set(),set(),set(),set()
        ans=0
        getNQueens(0,n)
        return ans