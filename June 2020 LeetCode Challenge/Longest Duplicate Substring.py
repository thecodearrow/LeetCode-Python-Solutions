#https://leetcode.com/problems/longest-duplicate-substring/


"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
"""


class Solution:
    def computeRollHash(self,s):
        #rolling hash array! 
        n=len(s)
        roll_hash=[0 for i in range(len(s))]
        roll_hash[0]=ord(s[0])-ord('a')+1
        p=31
        MOD=10**9+9
        power=[1]*n
        for i in range(1,len(s)):
            c=s[i]
            c_index=ord(c)-ord('a')+1
            roll_hash[i]=(c_index+(p*roll_hash[i-1]))%MOD
            power[i]=(power[i-1]*p)%MOD


        return roll_hash,power
    def substrRollHash(self,l,r,roll_hash,power):
        #r included
        p=31
        MOD=10**9+9
        if(l==0):
            return roll_hash[r]
        substr_roll_hash=roll_hash[r]-(roll_hash[l-1]*power[r-l+1])
        return substr_roll_hash%MOD
    def isDuplicateFound(self,s,l,roll_hash,power):
        MOD=10**9+9
        seen_roll_hashes={}
        current_roll_hash=self.substrRollHash(0,l-1,roll_hash,power)
        n=len(s)
        seen_roll_hashes[current_roll_hash]=0
        for i in range(l,len(s)):
            current_roll_hash=self.substrRollHash(i-l+1,i,roll_hash,power)
            if(current_roll_hash in seen_roll_hashes):
                idx=seen_roll_hashes[current_roll_hash]
                if(s[idx:idx+l]==s[i-l+1:i+1]):
                    return True,s[idx:idx+l]
            seen_roll_hashes[current_roll_hash]=i-l+1
        
        return False,""
            
        
        
    def longestDupSubstring(self, S: str) -> str:
        max_length=0
        start=1
        end=len(S)
        ans=""
        roll_hash,power=self.computeRollHash(S)
        while start<=end:
            mid=(start+end)//2
            #check if duplicate is found with length mid
            status,duplicate=self.isDuplicateFound(S,mid,roll_hash,power)
            if(status):
                ans=duplicate
                start=mid+1
            else:
                end=mid-1
        
        
        return ans