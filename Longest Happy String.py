class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def stringify(arr):
            return "".join(arr)
        max_heap=[]
        if(a>0):
            heapq.heappush(max_heap,(-a,'a'))
        if(b>0):
            heapq.heappush(max_heap,(-b,'b'))
        if(c>0):
            heapq.heappush(max_heap,(-c,'c'))
        ans=[]
        #greedy— place 2 chars with a delimiter
        while(max_heap):
            f,c=heapq.heappop(max_heap)
            f*=-1
            if(len(ans)<2):
                #add 2 c's
                ans.append(c)
                f-=1
                if(f>=1):
                    ans.append(c)
                    f-=1
                
            else:
                if(ans[-1]==ans[-2]==c):
                    #we need to place a delimiter! 
                    if(not max_heap):
                        #no more chars :( 
                        #return what we have longest possible! 
                        return stringify(ans)
                    df,dc=heapq.heappop(max_heap) #delimiter! 
                    df*=-1
                    df-=1
                    ans.append(dc)
                    if(df>0):
                        heapq.heappush(max_heap,(-df,dc))   #add the delimter back!
                    
                else:
                    ans.append(c)
                    f-=1
                    if(f>=1):
                        ans.append(c)
                        f-=1
                    
            if(f>0):
                heapq.heappush(max_heap,(-f,c))   #add the current back!
                
                
            
        return stringify(ans)
