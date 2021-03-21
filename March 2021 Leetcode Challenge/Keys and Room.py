#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/
from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=[0]
        visited=defaultdict(lambda:False)
        visited[0]=True
        while queue:
            u=queue.pop(0)
            for v in rooms[u]:
                if(not visited[v]):
                    queue.append(v)
                    visited[v]=True
                    
        
        for i in range(len(rooms)):
            if(not visited[i]):
                return False
        
        return True
                