#https://leetcode.com/problems/prefix-and-suffix-search/solution/

class SuffixWrappedTrie:
    def __init__(self):
        self.trie={}
    
    def insertSuffixWrapped(self,word,idx):
        suffix=""
        l=len(word)
        for i in range(l-1,-1,-1):
            suffix=word[i:l]
            #print(suffix+"#"+word)
            self.insert(suffix+"#"+word,idx) #suffix wrapped word 
    def insert(self,word,idx):
        trie=self.trie
        for c in word:
            if(c not in trie):
                trie[c]={}
            trie=trie[c]
            trie["idx"]=idx
            
        
        trie["*"]=idx #end of word!
    
    def isPresent(self,prefix):
        #returns the indices if prefix/suffix present, else -1
        trie=self.trie
        for c in prefix:
            if(c not in trie):
                return -1
            trie=trie[c]
        
        return trie["idx"]
            
            



class WordFilter:

    def __init__(self, words: List[str]):
        self.t=SuffixWrappedTrie()
        idx=0
        for w in words:
            self.t.insertSuffixWrapped(w,idx)
            idx+=1
    

    def f(self, prefix: str, suffix: str) -> int:
        query=suffix+"#"+prefix
        return self.t.isPresent(query)
        
                
            
        
            
        