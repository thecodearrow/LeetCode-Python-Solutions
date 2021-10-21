class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        #maintain a min heap
        scores=defaultdict(list) #top K
        k=5
        for id,score in items:
            heapq.heappush(scores[id],score)
            if(len(scores[id])>k):
                heapq.heappop(scores[id]) #remove minScore
        
        ans=[]
        for id in sorted(scores.keys()):
            avg5=sum(scores[id])//5
            ans.append([id,avg5])
        
        return ans
        
