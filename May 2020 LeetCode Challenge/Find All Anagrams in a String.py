#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls=len(s)
        lp=len(p)
        chars_count=Counter(p)
        i,j=0,0
        ans=[]
        while j<ls:
            if(chars_count[s[j]]>0):
                chars_count[s[j]]-=1
                j+=1
                if(j-i==lp):
                    ans.append(i)
            elif(i==j):
                i+=1
                j+=1
            elif(chars_count[s[j]]<=0):
                chars_count[s[i]]+=1
                i+=1
            
            
            
                
        return ans
        
#Alternate Solution, straight forward.... but the above solution is more optimal since we don't check the anagram count again and again


#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/


class Solution:
    def validAnagram(self,anagram_chars,chars_count):
        #every count of anagram_chars must be zero 
        #The time complexity of this function is O(26) at max
        for c in anagram_chars:
            if(chars_count[ord(c)-ord('a')]!=0):
                return False
            
        return True
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls=len(s)
        lp=len(p)
        anagram_chars=set(p) #the length can be at max 26
        if(lp>ls):
            return []
        chars_count=[0]*26
        i,j=0,0
        ans=[]
        for i in range(lp):
            cp=p[i]
            cs=s[i]
            chars_count[ord(cp)-ord('a')]+=1
            chars_count[ord(cs)-ord('a')]-=1
        if(self.validAnagram(anagram_chars,chars_count)):
            ans.append(0)
        
        for i in range(lp,ls):
            c_start=s[i-lp]
            c_end=s[i]
            chars_count[ord(c_start)-ord('a')]+=1
            chars_count[ord(c_end)-ord('a')]-=1
            current_window_start_index=i-lp+1
            if(self.validAnagram(anagram_chars,chars_count)):
                ans.append(current_window_start_index)
            
            
            
                
        return ans
        