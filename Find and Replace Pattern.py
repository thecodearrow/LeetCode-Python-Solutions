#https://leetcode.com/contest/weekly-contest-98/problems/find-and-replace-pattern/

from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans=[]
        
        pattern_match=[]
        num=0
        mapping={}
        for c in pattern:
            if(c not in mapping):
                num+=1
                mapping[c]=num
            pattern_match.append(mapping[c])
                
        for w in words:
            pattern_current=[]
            num=0
            mapping={}
            for c in w:
                if(c not in mapping):
                    num+=1
                    mapping[c]=num
                pattern_current.append(mapping[c])
            
            if(pattern_current==pattern_match):
                ans.append(w)
                
                    
        return ans
        
        
        
                
            
            
            
                
            
        
                
                