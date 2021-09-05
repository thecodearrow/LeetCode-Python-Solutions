class Solution:   
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        #sort based on decreasing attack, increasing defense
        #for every character even if you can find ONE other strong character, then it is weak!
        
        properties=sorted(properties,key=lambda x: (-x[0],x[1]))
        max_d=0
        weak=0
        for a,d in properties:
            if(max_d>d):
                weak+=1
            max_d=max(max_d,d)
        
        return weak
        
            
   
