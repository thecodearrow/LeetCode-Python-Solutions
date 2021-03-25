#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3683/

#Refer editorial!
#Basically after sorting A and B, if smallest ele in A > smallest ele in B.... then pair them up! 
#Allot the remainining ones arbitrarily!
from collections import defaultdict
class Solution:
    def findJustGreaterEle(self,given,A,alloted_a):
  
                
        return just_greater_ele,idx
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sorted_A=sorted(A)
        sorted_B=sorted(B)
        j=0
        alloted=defaultdict(list)
        remaining=[]
        for a in sorted_A:
            if(a>sorted_B[j]):
                alloted[sorted_B[j]].append(a)
                j+=1
            else:
                remaining.append(a)
                
        A_new=[]
        for b in B:
            if(alloted[b]):
                A_new.append(alloted[b].pop())
            else:
                A_new.append(remaining.pop())
                
        return A_new       
                
                        
                    