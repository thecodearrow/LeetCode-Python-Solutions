class BitTrie:
    def __init__(self):
        self.trie={}
    def insert(self,ele):
        trie=self.trie
        for i in range(32,-1,-1):
            d=(1<<i)&ele
            digit=1 if d else 0
            if(digit not in trie):
                trie[digit]={}
            trie=trie[digit]
        trie["*"]=True #marking the end of num
    def getMaxXOR(self,ele):
        trie=self.trie
        other=0
        for i in range(32,-1,-1):
            d=(1<<i)&ele
            if(d):
                #look for opposite bit to maximise xor
                if(0 in trie):
                    trie=trie[0]
                elif(1 in trie):
                    trie=trie[1]
                    other|=(1<<i)
                else:
                    return -1
            else:
                if(1 in trie):
                    trie=trie[1]
                    other|=(1<<i)
                elif(0 in trie):
                    trie=trie[0]
                else:
                    return -1
        xor=ele^other    
        return xor
            
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t=BitTrie()
        max_xor=0
        for ele in nums:
            xor=t.getMaxXOR(ele)
            if(xor!=-1):
                max_xor=max(max_xor,xor)
            t.insert(ele) #insert ele in bit trie
        
        return max_xor
