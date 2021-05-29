#https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/submissions/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #works well for any value of k in O(n) time. 
        n=len(s)
        k=3
        if(n<k):
            return 0
        
        #initial window
        unique={}
        unique_chars=0 #counter variable
        for i in range(k):
            if(s[i] not in unique):
                unique_chars+=1 #counter variable
            unique[s[i]]=i #map the occurring value of i! 
        good=0
        
        if(unique_chars==k):
            good=1
            
        
        #sliding window technique
        for i in range(k,n):
            if(unique[s[i-k]]==i-k):
                #hasn't occurred after this! (THINK wrt "aababcabc" )
                del unique[s[i-k]]
                unique_chars-=1 #decrement counter! 
                
            if(s[i] not in unique):
                unique_chars+=1 #increment counter!
            unique[s[i]]=i #map current char's index!
            if(unique_chars==k):
                good+=1  #if counter==k
            
        
        return good
                
            
            
        
        