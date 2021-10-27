class Solution:
    def isStrobo(self,num,strobo):
        #Approach One
        rotated=[]
        for c in reversed(num):
            #you have to process in reverse
            if(not strobo[c]):
                return False
            rotated.append(strobo[c])
        rotated="".join(rotated)
        return rotated==num
    def isStrobogrammatic(self, num: str) -> bool:
        strobo={'0':'0','1':'1','2':False,'3':False,'4':False,'5':False,'6':'9','7':False,'8':'8','9':'6'}
        
        #Approach2 — 2 pointer role 
        l=0
        r=len(num)-1
        while l<=r:
            rotated_left=strobo[num[l]]
            if(rotated_left!=num[r]):
                return False
            l+=1
            r-=1
        return True
        #return self.isStrobo(num,strobo)
