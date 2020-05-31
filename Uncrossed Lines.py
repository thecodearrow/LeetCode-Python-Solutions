"""
#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

"""

#This is just a LCS problem! 
from collections import defaultdict,Counter

class Solution:
    def maxLines(self,i,j,l1,l2,A,B,cache):
        if(i==l1 or j==l2):
            return 0
        key=hash((i,j))
        if(key in cache):
            return cache[key]
        choice3=0
        if(A[i]==B[j]):
            cache[key]=1+self.maxLines(i+1,j+1,l1,l2,A,B,cache)
        else:
            choice1=self.maxLines(i,j+1,l1,l2,A,B,cache)
            choice2=self.maxLines(i+1,j,l1,l2,A,B,cache)
            cache[key]=max(choice1,choice2)
        return cache[key]
        
            
        
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        #eliminate values that don't contribute a line! 
        new_A=[] 
        new_B=[] 
        present_in_a=Counter(A)
        present_in_b=Counter(B)#hashmap for B
        for ele in A:
            if(ele in present_in_b):
                new_A.append(ele) 
    
        for ele in B:
            if(ele in present_in_a):
                new_B.append(ele)
                
        return self.maxLines(0,0,len(new_A),len(new_B),new_A,new_B,{})
class Solution1:
    def maxLines(self,index,n,A,current_boundary,cache):
        if(index==n):
            return 0
        key=hash((index,current_boundary))
        if(key in cache):
            return cache[key]
        ele,partners=A[index]
        choice1=0
        for p in partners:
            #partners are choices for lines for ele
            if(p>current_boundary):
                #can make a line!
                choice1=max(choice1,1+self.maxLines(index+1,n,A,p,cache)) #update current boundary!
        choice2=self.maxLines(index+1,n,A,current_boundary,cache) #no line from ele
        cache[key]=max(choice1,choice2)
        return cache[key]
        
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        new_A=[] #eliminate elements which don't contribute a line
        present_at=defaultdict(list) #hashmap for B
        for i,ele in enumerate(B):
            present_at[ele].append(i)
        for ele in A:
            if(ele in present_at):
                new_A.append([ele,present_at[ele]]) #element in A and it's partner's location in B
        
        
        current_boundary=-1 #cannot intersect even at end points
        return self.maxLines(0,len(new_A),new_A,current_boundary,{})