class Trie:
    def __init__(self):
        self.trie={}
    def insert(self,binary_string):
        trie=self.trie
        for c in binary_string:
            if(c not in trie):
                trie[c]={}
            trie=trie[c]
        
        trie["*"]=True 
    
    def findUnique(self,i,current,n,trie):
        global ans 
        if("0" not in trie):
            #ans found
            current.append("0")
            r=n-i-1 #pad right with zeros
            current+=["0"]*r
            ans="".join(current)
            return 
        if("1" not in trie):
            #ans found!
            current.append("1")
            r=n-i-1 #pad right with zeros
            current+=["0"]*r
            ans="".join(current)
            return
        self.findUnique(i+1,current+['0'],n,trie['0'])
        self.findUnique(i+1,current+['1'],n,trie['1'])
        
        
        
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        #Approach 1 Trie based approach! 
        #Trying to generate binary string with the help of a trie
        
        # global ans
        # ans=""
        # t=Trie()
        # for b in nums:
        #     t.insert(b)
        # n=len(nums)
        # t.findUnique(0,[],n,t.trie)
        # return ans
        
        #Approach2 Set different bit for ith position and keep iterating through nums
        #This way the resultant number is unique! 
        n=len(nums)
        i=0
        unique=['']*n
        for i in range(n):
            bit=nums[i][i]
            if(bit=='0'):
                #bit is zero, set unique's ith bit to one
                unique[i]='1'
            else:
                unique[i]='0' 
            
        unique="".join(unique)
        return unique
            
                
        
