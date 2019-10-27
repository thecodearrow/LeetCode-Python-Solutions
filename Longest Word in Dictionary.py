#https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.letters={}
    def addString(self,s):
        letters=self.letters
        for c in s:
            if(c not in letters):
                letters[c]={}
            letters=letters[c]
            
        letters["."]=True
    
    def containsEveryPrefix(self,s):
        letters=self.letters
        for c in s:
            if(c in letters):
                letters=letters[c]
                if("." not in letters):
                    return False
            else:
                return False
        return True
            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t=Trie()
        words=sorted(words)
        for w in words:
            t.addString(w)
        maxLength=0
        ans=""
        for w in words:
            currentLength=len(w)
            if(t.containsEveryPrefix(w)):
                if(currentLength>maxLength):
                    maxLength=currentLength
                    ans=w
                
            
        return ans
                
                