#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1="0"+word1
        word2="0"+word2
        l1=len(word1)
        l2=len(word2)
        edits=[[0 for j in range(l2)]for i in range(l1)]
        for j in range(1,l2):
            edits[0][j]=edits[0][j-1]+1
        for i in range(1,l1):
            edits[i][0]=edits[i-1][0]+1
        for i in range(1,l1):
            for j in range(1,l2):
                if(word1[i]==word2[j]):
                    edits[i][j]=edits[i-1][j-1]
                else:
                    edits[i][j]=1+min(edits[i-1][j-1],edits[i-1][j],edits[i][j-1])
                
        return edits[l1-1][l2-1]