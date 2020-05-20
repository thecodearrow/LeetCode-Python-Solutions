"""
#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

This can be solved using one observation....

Say the array is 1,1,3,4,4,5,5
The indices are: 0 1 2 3 4 5 6

The key here is before the single element... all duplicate pairs occur at (even,odd) indices...
For example: (1,1) occurs at (0,1) which is even odd

After the single element... all duplicate pairs occur at (odd,even) indices...
For example: (4,4) occurs at (3,4) which is odd,even

So we can use binary search using this observation. 

If we get a (even,odd) duplicate we move right since the single element is on the right side..
else if we get a (odd,even) duplicate we move left since the single element is on the left side



"""

class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n=len(A) 
        start=0
        end=n-1
        
        while(start<=end):
            mid=start+(end-start)//2
            if(mid==0 or mid==n-1):
                #we have reached the start or end of the array! 
                #that means our single element must be at the ends
                return A[mid] #single element
 
            else:
                #middle elements
                if(A[mid]!=A[mid-1] and A[mid]!=A[mid+1]):
                    return A[mid] #single element
                else:
                    #duplicate pair!
                    dupli_index=mid
                    if(A[mid-1]==A[mid]):
                        #mid holds the second duplicate
                        dupli_index=mid-1 #we want the index of the first duplicate
                    
                    if(dupli_index%2==0):
                        #even odd
                        start=mid+1 #move right
                    else:
                        end=mid-1 #move left
                        
                
                
                
                    
            
        
        