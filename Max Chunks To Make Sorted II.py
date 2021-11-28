class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        #using leftMax and rightMin arr! 
        n=len(arr)
        leftMax=[0]*n
        leftMax[0]=arr[0]
        rightMin=[0]*n
        rightMin[n-1]=arr[n-1]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],arr[i])
        
        for i in range(n-2,-1,-1):
            rightMin[i]=min(rightMin[i+1],arr[i])
            
        chunks=1
        for i in range(1,n):
            if(leftMax[i-1]<=rightMin[i]):
                chunks+=1
        
        return chunks
