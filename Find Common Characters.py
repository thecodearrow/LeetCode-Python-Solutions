class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])
        n=len(words)
        for i in range(1,n):
            word=words[i]
            current_word=Counter(word)
            for c in common:
                if(c not in current_word):
                    f=0
                else:
                    f=current_word[c]
                new_f=min(f,common[c])
                common[c]=new_f
        
        ans=[] #common_chars
        for c in common:
            if(common[c]>0):
                for i in range(common[c]):
                    ans.append(c)
            
            
            
        
        return ans
