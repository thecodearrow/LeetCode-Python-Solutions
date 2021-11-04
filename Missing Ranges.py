class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def stringify(l,h):
            if(l==h):
                return str(l)
            else:
                return str(l)+"->"+str(h)
        n=len(nums)
        if(n==0):
            return [stringify(lower,upper)]
        ranges=[]
        
        for i in range(-1,n):
            l=nums[i]+1 if i>=0 else lower
            h=nums[i+1]-1 if(i<n-1) else upper
            if(l<=h):
                ranges.append(stringify(l,h))
            
        return ranges
        
