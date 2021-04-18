#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3687/

from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        numbers=[0, 2, 4, 6, 8, 1, 3, 5, 7, 9] #order matters
        chars=Counter(s)
        ans=""
        numToEnglish={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        counter=0
        found=[0]*10
        while counter<10:
            i=numbers[counter]
            eng=numToEnglish[i]
            present=True
            for c in eng:
                if(c not in chars or chars[c]==0):
                    present=False
                    break
            if(present):
                found[i]+=1
                #remove chars from set
                for c in eng:
                    chars[c]-=1
            else:
                counter+=1

                #print(chars)
        
        for i in range(10):
            ans+=str(i)*found[i]
        return ans
                
            
            
            