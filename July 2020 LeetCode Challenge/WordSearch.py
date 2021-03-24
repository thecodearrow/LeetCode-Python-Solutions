"""
#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def searchForWord(self,index,i,j,l,n,m,word,board,seen):
        if(index==l):
            return True
        if(i<0 or j<0 or i==n or j==m):
            return False
        if(word[index]!=board[i][j]):
            return False
        if(seen[i][j]):
            return False
        seen[i][j]=True
        status=self.searchForWord(index+1,i+1,j,l,n,m,word,board,seen) or self.searchForWord(index+1,i-1,j,l,n,m,word,board,seen) or self.searchForWord(index+1,i,j+1,l,n,m,word,board,seen) or self.searchForWord(index+1,i,j-1,l,n,m,word,board,seen)
        seen[i][j]=False
        return status
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        l=len(word)
        seen=[]
        for i in range(n):
            seen.append([])
            for j in range(m):
                seen[i].append(False)
                
        for i in range(len(board)):
            for j in range(len(board[0])): 
                if(self.searchForWord(0,i,j,l,n,m,word,board,seen)):
                    return True
        return False
        