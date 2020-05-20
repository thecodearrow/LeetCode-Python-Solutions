#https://leetcode.com/problems/word-search-ii/submissions/

class Trie:
	def __init__(self):
		self.trie={}
		
	def add(self,word):
		trie=self.trie
		for c in word:
			if(c not in trie):
				trie[c]={}
			trie=trie[c]
		
		trie["*"]=word #end of word! 
			
		
class Solution:
    def explore(self,trie,i,j,n,m,board,found_words):
        if(i<0 or j<0 or i>=n or j>=m):
            return
        c=board[i][j]
        if(c not in trie):
            #no word can be formed from current i,j
            return

        if(board[i][j]=="0"):
            return
        trie=trie[c]
        if("*" in trie):
            #word present in trie
            word=trie["*"]
            found_words[word]=True

        board[i][j]="0"#mark visited
                #4 directions
        self.explore(trie,i-1,j,n,m,board,found_words)
        self.explore(trie,i+1,j,n,m,board,found_words)
        self.explore(trie,i,j+1,n,m,board,found_words)
        self.explore(trie,i,j-1,n,m,board,found_words)
        board[i][j]=c #backtrack! 

	
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n=len(board)
        m=len(board[0])
        t=Trie()
        for w in words:
            t.add(w)
        found_words={}
        for i in range(n):
            for j in range(m):
                self.explore(t.trie,i,j,n,m,board,found_words)
        return list(found_words)


