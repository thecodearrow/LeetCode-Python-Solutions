class Solution:
    def rotate(self,num,strobo):
        rotated=[]
        for c in reversed(num):
            if(not strobo[c]):
                return False,""
            rotated.append(strobo[c])
        rotated="".join(rotated)
        return True,rotated
    def isStrobogrammatic(self, num: str) -> bool:
        strobo={'0':'0','1':'1','2':False,'3':False,'4':False,'5':False,'6':'9','7':False,'8':'8','9':'6'}
        status,rotated=self.rotate(num,strobo)
        return status and rotated==num
