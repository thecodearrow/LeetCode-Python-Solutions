class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l=len(changed)
        if(l%2!=0):
            return []
        changed=sorted(changed) #needs sorting for it work
        seen=defaultdict(lambda:0)
        original=[]
        for ele in changed:
            half_ele=ele/2
            if(seen[half_ele]==0):
                original.append(ele)
                seen[ele]+=1
            else:
                seen[half_ele]-=1
            
        return original if len(original)==l/2 else []
