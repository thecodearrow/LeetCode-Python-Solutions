class Solution:

    def getStroboCount(self,i,number_first,number_second,half_limit,n,strobo):
        if(i==half_limit):
            global ans
            number=number_first[:]+number_second[::-1] #reverse second half
            number="".join(number)
            ans.append(number)
            return
        for d in strobo:
            if(i==0 and d=='0'):
                #first digit shouldn't be a zero! 
                continue
            if(n%2!=0 and i==half_limit-1):
                #single middle char for odd n
                if(d!='6' and d!='9'):
                    #cannot add '6' and '9' (MOST IMPORTANT! )
                    number_first.append(d)
                    self.getStroboCount(i+1,number_first,number_second,half_limit,n,strobo)
                    number_first.pop()
            else:
                number_first.append(d)
                number_second.append(strobo[d])
                self.getStroboCount(i+1,number_first,number_second,half_limit,n,strobo)
                number_first.pop()
                number_second.pop()
            
            
        
    def findStrobogrammatic(self, n: int) -> List[str]:
        #Generate half strobo number! 
        #Solve Strobogrammatic Number I using 2 pointer to get a hint
        half_limit=n//2 if n%2==0 else (n//2) +1
        if(n==1):
            return ["0","1","8"]
        strobo={'0':'0','1':'1','6':'9','8':'8','9':'6'} #strobo digits and their 180 deg mapping! 
        global ans
        ans=[]
        self.getStroboCount(0,[],[],half_limit,n,strobo)
        return ans
