#Uncommon Words from Two Sentences

from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count=defaultdict(lambda:0)
        
        sentence=A+" "+B
        words=sentence.split(" ")
        for w in words:
            count[w]+=1
            
        ans=[]
        for w in words:
            if(count[w]==1):
                ans.append(w)
        
        return ans