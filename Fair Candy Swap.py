#Say the ans is [a,b]

#S1-a+b=S2-b+a

#=> S1-S2=2(a-b)  

#a is an element in array 1. Check for every a, a suitable b exists!

class Solution:
    def fairCandySwap(self, A, B):
        diff=sum(B)-sum(A)
        set_b=set()
        for b in B:
            set_b.add(b)
            
        for ele in A:
            other_ele=(diff+2*ele)/2
            other_ele=int(other_ele)
            if(other_ele in set_b):
                return [ele,other_ele]
        
        