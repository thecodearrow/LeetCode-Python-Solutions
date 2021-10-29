class Solution:
    def minDeletions(self, s: str) -> int:
        count=Counter(s)
        counts=[]
        for c in count:
            counts.append((c,count[c]))
        counts.sort(key=lambda x:x[1],reverse=True)
        seen_freq=set()
        deletes=0
        for c,f in counts:
            while(f>0. and f in seen_freq):
                deletes+=1
                seen_freq.add(f)
                f-=1
            seen_freq.add(f)
        
        return deletes
