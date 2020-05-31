#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_length=0
        char_map=[0]*26
        for c in chars:
            char_map[ord(c)-ord('a')]+=1
        for word in words:
            lookup=list(char_map)
            is_good=True
            for c in word:
                if(lookup[ord(c)-ord('a')]==0):
                    is_good=False
                    break
                lookup[ord(c)-ord('a')]-=1
                
            if(is_good):
                good_length+=len(word)
                
        
        return good_length