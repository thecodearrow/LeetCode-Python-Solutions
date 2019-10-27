#https://leetcode.com/problems/permutation-in-string/submissions/
#Using Hash Function
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        hash1=0
        for c in s1:
            hash1+=hash(c)
        hash2=0
        for c in s2[:l1]:
            hash2+=hash(c)
        if(hash1==hash2):
            return True
        for i in range(l1,l2):
            hash2+=hash(s2[i])
            hash2-=hash(s2[i-l1])
            if(hash1==hash2):
                return True
            
        
        return False
            

#Sliding Window with lookup array approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        freq1=[0]*26
        freq2=[0]*26
        for c in s1:
            freq1[ord(c)-ord('a')]+=1
        for c in s2[:l1]:
            freq2[ord(c)-ord('a')]+=1
            
        if(freq1==freq2):
            return True
        for i in range(l1,l2):
            current_char=s2[i]
            to_remove_char=s2[i-l1]
            freq2[ord(current_char)-ord('a')]+=1
            freq2[ord(to_remove_char)-ord('a')]-=1
            if(freq1==freq2):
                return True
            
        
        return False
            