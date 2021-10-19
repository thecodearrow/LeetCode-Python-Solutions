class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l1=len(s)
        l2=len(t)
        if(l1>l2):
            #ensure t is longer than s
            return self.isOneEditDistance(t,s)
        
        #edge cases! 
        if(l2-l1>1):
            return False
        if(l1==l2 and s==t):
            #zero edits away
            return False
        

        #now check if t is off by s by at most one
        edits=0
        i=0
        j=0
        isSameLength=(l1==l2)
        while i<l1 and j<l2:
            if(s[i]==t[j]):
                i+=1
                j+=1
            else:
                if(edits==1):
                    #requires more than one edit
                    return False
                edits+=1
                if(isSameLength):
                    i+=1
                j+=1
                
        return True
        
