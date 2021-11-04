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
        if(lower<nums[0]):
            ranges.append(stringify(lower,nums[0]-1)) #first missing range
        for i in range(n-1):
            l=nums[i]+1
            h=nums[i+1]-1
            if(l<=h):
                ranges.append(stringify(l,h))
        if(upper>nums[-1]):
            ranges.append(stringify(nums[-1]+1,upper)) #last missing range
            
        return ranges
        
