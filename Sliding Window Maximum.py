from collections import deque
import heapq
class Solution:
    def solutionUsingHeap(self,nums,k):
        #using heap
        window=[] #(ele,idx)
        n=len(nums)
        for i in range(k):
            heapq.heappush(window,(-nums[i],i))
        currMax,currIdx=heapq.heappop(window)
        if(currIdx!=0):
            #reinsert!
            heapq.heappush(window,(currMax,currIdx))
        ans=[-currMax]
        
        
        for i in range(k,n):
            heapq.heappush(window,(-nums[i],i))
            currMax,currIdx=window[0]
            while currIdx<=(i-k):
                #out of order! 
                currMax,currIdx=heapq.heappop(window)
            if(currIdx>i-k+1):
                #reinsert! 
                heapq.heappush(window,(currMax,currIdx))
            ans.append(-currMax)
            
            

        return ans
    
    def solutionUsingDeque(self,nums,k):
        n=len(nums)
        window=deque()
        ans=[]
        for i in range(k):
            while(window and nums[i]>=window[-1][0]):
                currEle,currIdx=window.pop()
            window.append((nums[i],i))
            
            
        #the item at the beginning is always the current_max
        currMax,currIdx=window[0]
        ans.append(currMax)
        for i in range(k,n):
            currEle,currIdx=window[0]
            #remove out of order indices from the beginning!
            if(window and currIdx<=(i-k)):
                currEle,currIdx=window.popleft()
                
            #remove no longer needed elements from the end!
            while(window and nums[i]>=window[-1][0]):
                window.pop()
            window.append((nums[i],i))
            ans.append(window[0][0]) #currMax
            
            
        return ans
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #return self.solutionUsingHeap(nums,k)
        return self.solutionUsingDeque(nums,k)