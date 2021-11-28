class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        def makeChunks(start,end,n,present):
            if(end==n):
                #we've reached the end of array! 
                return 0
            present.add(arr[end])
            #find if all numbers from start to end exist! 
            for i in range(start,end+1):
                if(i not in present):
                    return makeChunks(start,end+1,n,present)
            
            return 1+makeChunks(end+1,end+1,n,present) #make a chunk! 
        
        
        #Approach1 (using recursion!)
        #present=set()
        #return makeChunks(0,0,n,present)
    
        
        #Approach2 
        chunks=0
        currentMax=0
        for i in range(n):
            currentMax=max(currentMax,arr[i])
            if(currentMax==i):
                #now all elements from A[0:i+1] is present! 
                chunks+=1
           
        
        return chunks
            
