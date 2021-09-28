class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #same as aggressive cows problem! 
        #binary search on the possible force value
        #m balls, 
        position=sorted(position) #the postions have to be sorted.... also eliminates the need to take abs
        
        def isPossible(force):
            #is it possible to place balls with atleast this force! 
            n=len(position)
            balls=1 #first ball placed at bin 0
            last_pos=position[0]
            i=1
            for i in range(1,n):
                current_f=position[i]-last_pos
                if(current_f>=force):
                    #place ball
                    balls+=1
                    if(balls==m):
                        #have placed all balls already before completing all bins! 
                        return True
                    last_pos=position[i]
             
            
            return balls==m
                    
                
            
        
        low=1
        high=position[-1]-position[0]
        ans=1
        while low<=high:
            mid=(low+high)//2 #current force
            if(isPossible(mid)):
                #is force possible! 
                #try making it larger
                low=mid+1
                ans=max(ans,mid)
            else:
                #try making it smaller
                high=mid-1
        
        return ans
        
                
        
        
