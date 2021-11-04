class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        def stringify(l,h):
            if(l==h):
                return str(l)
            else:
                return str(l)+"->"+str(h)
        if(n==0):
            return []
        l=nums[0]
        h=nums[0]
        ranges=[]
        for i in range(1,n):
            if(nums[i]-nums[i-1]==1):
                h+=1
            else:
                ranges.append(stringify(l,h))
                l=nums[i]
                h=nums[i]
        
        ranges.append(stringify(l,h))
        return ranges
