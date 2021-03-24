#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3682/

from collections import Counter
class Solution:
    
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        def nc3(n):
            return (n*(n-1)*(n-2))//6
        
        def nc2(n):
            return n*(n-1)//2
        ans=0
        cnt=Counter(arr)
        MOD=10**9+7
        n=101 #range of arr
        #also ensure you're proceeding in one direction and counting once (with combinatorics!)
        for i in range(n):
            for j in range(i,n):
                k=target-i-j
                if(k>=0 and k<=100):
                    #in range
                    if(cnt[i]>0 and cnt[j]>0 and cnt[k]>0):
                        #exists!
                        if(i==j==k):
                            #nc3
                            ans+=nc3(cnt[i])
                        elif(i==j):
                            ans+=nc2(cnt[i])*cnt[k]
                        elif(i<j and j<k):
                            ans+=cnt[i]*cnt[j]*cnt[k]

                        ans%=MOD
        
        return ans
                    
                
        