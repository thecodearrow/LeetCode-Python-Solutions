#https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        n=len(A)
        if(n==0):
            return 0
        if(n==1):
            return A[0]
        stack=[0]
        idx=1
        maxArea=0
        while idx<n:
            currentHeight=A[idx]
            topElementHeight=A[stack[-1]]
            if(not stack or topElementHeight<=currentHeight):
                stack.append(idx)
            else:
                while(stack and A[stack[-1]]>currentHeight):
                    poppedElementIdx=stack.pop()
                    if(stack):
                        contributedArea=A[poppedElementIdx]*(idx-stack[-1]-1)
                    else:
                        contributedArea=A[poppedElementIdx]*idx
                    maxArea=max(contributedArea,maxArea)
                    
                stack.append(idx)
        
            idx+=1
            
        #For the remaining elements in stack!
        while(stack):
            poppedElementIdx=stack.pop()
            if(stack):
                contributedArea=A[poppedElementIdx]*(idx-stack[-1]-1)
            else:
                contributedArea=A[poppedElementIdx]*idx
            maxArea=max(contributedArea,maxArea)
        return maxArea