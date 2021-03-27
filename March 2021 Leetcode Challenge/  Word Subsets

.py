#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3685/

from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universal=[]
        new_B={} #union of all words in B
        for b in B:
            freq_b=Counter(b)
            for c in freq_b:
                if(c not in new_B):
                    new_B[c]=freq_b[c]
                else:
                    new_B[c]=max(new_B[c],freq_b[c])
        
        for a in A:
            candidate=True
            freq_a=Counter(a)
            for b in new_B:
                if(b not in freq_a or freq_a[b]<new_B[b]):
                    candidate=False
                    break
                        
            if(candidate):
                universal.append(a)
                
        
        return universal
        