#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3762/

class Trie:
    def __init__(self):
        self.trie={}
    
    def addWord(self,word):
        trie=self.trie
        for c in word:
            if(c not in trie):
                trie[c]={"startsWith":[]}
            if(len(trie[c]["startsWith"])<3):
                trie[c]["startsWith"].append(word)
            trie=trie[c]
        
        trie["*"]=True
    
    def search(self,word):
        lookup=[] #list of list
        trie=self.trie
        for c in word:
            if(c not in trie):
                break
            else:
                foundWords=trie[c]["startsWith"]
                lookup.append(foundWords)
                trie=trie[c]
        
        remaining=len(word)-len(lookup)
        for i in range(remaining):
            lookup.append([])
        return lookup

    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t=Trie()
        products.sort() #sorting helps insert lexicographically! 
        for p in products:
            t.addWord(p)
        
        return t.search(searchWord)
        
        