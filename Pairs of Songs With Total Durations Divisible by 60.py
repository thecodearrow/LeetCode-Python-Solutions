class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time=[t%60 for t in time] #mod 60
        freq=Counter(time)
        ans=0
        seen=set()
        for ele in freq:
            if(ele not in seen):
                comple=(60-ele)
                seen.add(ele)
                seen.add(comple)
                if(ele==0 or ele==30):
                    #edge cases! 
                    f=freq[ele]
                    ans+=(f*(f-1))//2
                else:
                    f1=freq[ele]
                    f2=freq[comple]
                    ans+=f1*f2
        
        return ans
