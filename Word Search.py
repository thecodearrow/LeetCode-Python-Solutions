#https://leetcode.com/problems/word-search/submissions/

class Solution:
        def explore(self,word,index,l,i,j,n,m,board,visited):
            if(index==l):
                #word present
                return True
            if(i<0 or j<0 or i>=n or j>=m):
                return False
            
            if(word[index]!=board[i][j]):
                return False
            if(visited[i][j]):
                return False
            visited[i][j]=True
            status=False
            status=status or self.explore(word,index+1,l,i,j-1,n,m,board,visited)
            status=status or self.explore(word,index+1,l,i,j+1,n,m,board,visited)
            status=status or self.explore(word,index+1,l,i-1,j,n,m,board,visited)
            status=status or self.explore(word,index+1,l,i+1,j,n,m,board,visited)
            visited[i][j]=False
            return status
        def exist(self, board: List[List[str]], word: str) -> bool:
            n=len(board)
            m=len(board[0])
            l=len(word)
            visited=[[False for i in range(m)]for j in range(n)]
            for i in range(n):
                for j in range(m):
                    if(word[0]==board[i][j]):
                        #small opimisation!
                        if(self.explore(word,0,l,i,j,n,m,board,visited)):
                            return True

            return False