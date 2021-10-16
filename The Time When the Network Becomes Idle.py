
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n=len(patience)
        nbrs=defaultdict(list)
        for u,v in edges:
            nbrs[u].append(v)
            nbrs[v].append(u)
            
        source=0
        visited=defaultdict(lambda:False)
        visited[0]=True
        queue=[(source)]
        dist=defaultdict(lambda:0)
        while queue:
            u=queue.pop(0)
            for v in nbrs[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)
                    dist[v]=dist[u]+1
        
        idle_time=0
        neg=0
        for i in range(1,n):
            t=dist[i]*2
            p=min(patience[i],t)
            x=(t//p) #no of messages! 
            last_message_start_time=x*p
            if(last_message_start_time==t):
                #edge case! 
                last_message_start_time=(x-1)*p #send one message less
            last_message_end_time=last_message_start_time+t
            idle_time=max(idle_time,last_message_end_time)

            
        return 1+idle_time
            
