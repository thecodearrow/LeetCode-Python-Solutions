#https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if(len(s)!=len(t)):
            return False
        for c in s:
            if(c not in freq):
                freq[c]=1
            else:
                freq[c]+=1
        
        for c in t:
            if(c not in freq):
                freq[c]=-1
            else:
                freq[c]-=1
                
        for key in freq:
            if(freq[key]!=0):
                return False
            
        return True