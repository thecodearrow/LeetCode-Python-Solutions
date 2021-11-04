class Trie:
    def __init__(self):
        self.trie={}
    def addSentence(self,sentence,weight):
        trie=self.trie
        sentence_hash=hash(sentence)
        for c in sentence:
            if(c not in trie):
                trie[c]={"sentences":[],"freq":{}}
            trie=trie[c]
            if(sentence_hash not in trie["freq"]):
                trie["sentences"].append(sentence) #append sentence!
                trie["freq"][sentence_hash]=0 #init
            trie["freq"][sentence_hash]+=weight
    
    def getTop3(self,sentence):
        trie=self.trie
        top=[]
        for c in sentence:
            if(c not in trie):
                return []
            trie=trie[c]
        
        for s in trie["sentences"]:
            s_hash=hash(s)
            wt=trie["freq"][s_hash]
            top.append((wt,s))
        
        #can be optimised to O(NlogK) using a heap! 
        top=sorted(top,key=lambda x:(-x[0],x[1]))
        top_3=[]
        for w,s in top[:3]:
            top_3.append(s)
        return top_3
        
    
            
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie=Trie()
        for s,w in zip(sentences,times):
            self.trie.addSentence(s,w)
        
        self.current=[] #current_sentence

    def input(self, c: str) -> List[str]:
        if(c=="#"):
            sentence="".join(self.current)
            self.trie.addSentence(sentence,1) 
            self.current=[] #reset 
            return 
        self.current.append(c)
        #print(self.current)
        #print("...")
        #print(self.trie.trie)
        top_3=self.trie.getTop3(self.current)
        return top_3
        
        
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
