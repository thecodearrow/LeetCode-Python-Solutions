#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/

class Solution: 
    def isPali(self,word):
        i=0
        j=len(word)-1
        while i<j:
            if(word[i]!=word[j]):
                return False
            i+=1
            j-=1
        return True
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n=len(words)
        palindromes=set()
        lookup={word:i for i,word in enumerate(words)} #word lookup!
        for i,word in enumerate(words):
            if(len(word)>0):
                r_word=word[::-1]
                if(r_word in lookup):
                    r_i=lookup[r_word]
                    if(r_i!=i):
                        palindromes.add((r_i,i))
                        palindromes.add((i,r_i))

                #forward
                first=""
                for j in range(len(word)):
                    first+=word[j]
                    second=word[j+1:] #also handles the empty string edge case! 
                    rev_first=first[::-1]
                    rev_second=second[::-1]
                    if(rev_second in lookup  and  self.isPali(first)):
                        l_i=lookup[rev_second]
                        if(l_i!=i):
                            palindromes.add((l_i,i))
                            if(rev_second==""): #edge case!
                                palindromes.add((i,l_i))
                    if(rev_first in lookup  and  self.isPali(second)):
                        l_i=lookup[rev_first]
                        if(l_i!=i):
                            palindromes.add((i,l_i))
                            if(rev_first==""): #edge case!
                                palindromes.add((i,l_i))
                    
                
              
                
               
                
            
            
            
        
        
        
        return [[i,j] for i,j in palindromes]
                        
                        
                    
                    
        