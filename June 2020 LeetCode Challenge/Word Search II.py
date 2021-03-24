"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3376/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

"""
class Trie:
    def __init__(self):
        self.trie={}
    
    def insertWord(self,word):
        trie=self.trie
        for c in word:
            if(c not in trie):
                trie[c]={}
            trie=trie[c]
        trie["*"]=word 
    
    
class Solution:
    def startTraversing(self,i,j,n,m,board,trie,visited):
        if(i<0 or j<0 or i==n or j==m):
            return
        current_char=board[i][j]
        if(visited[(i,j)]):
            return
        if(current_char not in trie):
            return
        trie=trie[current_char]
        if("*" in trie):
            #we have found the word
            global foundWords
            foundWords.add(trie["*"])
            
            
        
       
        visited[(i,j)]=True
        self.startTraversing(i,j+1,n,m,board,trie,visited)
        self.startTraversing(i,j-1,n,m,board,trie,visited)
        self.startTraversing(i-1,j,n,m,board,trie,visited)
        self.startTraversing(i+1,j,n,m,board,trie,visited)
        visited[(i,j)]=False
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t=Trie()
        for word in words:
            t.insertWord(word)
        global foundWords
        foundWords=set()
        n=len(board)
        m=len(board[0])
        
        
        for i in range(n):
            for j in range(m):
                visited=defaultdict(lambda:False)
                self.startTraversing(i,j,n,m,board,t.trie,visited)
        
        return foundWords
                