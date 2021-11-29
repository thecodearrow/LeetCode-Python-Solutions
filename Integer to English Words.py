class Solution:
    def getDigits(self,n):
        digits=[]
        while n:
            d=n%10
            n//=10
            digits.append(d)

        return digits[::-1]
    def ones(self,n):
        mapping={0:'Zero',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        return mapping[n] if n in mapping else ""
    
    def underTwenty(self,n):
        mapping={10:'Ten',11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        return mapping[n] if n in mapping else ""
    
    def tens(self,n):
        mapping={10:'Ten',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        return mapping[n] if n in mapping else ""
        
    def twoDigits(self,n):
        #10-99
        if(10<=n <20):
            #edge case #10-19
            return self.underTwenty(n)
        digits=self.getDigits(n)
        l=len(digits)
        if(l==0):
            return ""
        elif(l==1):
            #Example 02, 03
            return self.ones(digits[0])
        else:
            ans=self.tens(digits[0]*10)
            if(digits[1]==0):
                return ans
            ans+=" "+self.ones(digits[1])
            return ans
         
    def threeDigits(self,n):
        #100-999
        digits=self.getDigits(n)
        l=len(digits)
        if(l<3):
            return self.twoDigits(n)
        else:
            #300, 400,500
            third,second,first=digits[0],digits[1],digits[2]
            if(first==0 and second==0):
                return self.ones(third)+" Hundred"
            else:
                #302, 323 
                remaining=second*10+first #remaining2 digits!
                return self.ones(third)+" Hundred "+self.twoDigits(remaining)
        
        return ""
    
    def thousands(self,n):
        digits=self.getDigits(n)
        l=len(digits)
        if(l<4):
            return self.threeDigits(n)
        if(l==4):
            first=digits[0]
            rem=n-first*1000
            ans=self.ones(first)+" Thousand"
            remString=self.threeDigits(rem)
            if(remString!=""):
                ans+=" "+remString
    
            return ans
        elif(l==5):
            firstTwo=digits[0]*10+digits[1]
            rem=n-firstTwo*1000
            ans=self.twoDigits(firstTwo)+" Thousand"
            remString=self.threeDigits(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        elif(l==6):
            firstThree=digits[0]*100+digits[1]*10+digits[2]
            rem=n-firstThree*1000
            ans=self.threeDigits(firstThree)+" Thousand"
            remString=self.threeDigits(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        return ""
    def millions(self,n):
        digits=self.getDigits(n)
        l=len(digits)
        if(l<7):
            return self.thousands(n)
        elif(l==7):
            first=digits[0]
            rem=n-first*10**6
            ans=self.ones(first)+" Million"
            remString=self.thousands(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        elif(l==8):
            firstTwo=digits[0]*10+digits[1]
            rem=n-firstTwo*10**6
            ans=self.twoDigits(firstTwo)+" Million"
            remString=self.thousands(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        elif(l==9):
            firstThree=digits[0]*100+digits[1]*10+digits[2]
            rem=n-firstThree*10**6
            ans=self.threeDigits(firstThree)+" Million"
            remString=self.thousands(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        return ""
            
    def billions(self,n):
        digits=self.getDigits(n)
        l=len(digits)
        if(l<10):
            return self.millions(n)
        if(l==10):
            first=digits[0]
            rem=n-first*10**9
            ans=self.ones(first)+" Billion"
            remString=self.millions(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        elif(l==11):
            firstTwo=digits[0]*10+digits[1]
            rem=n-firstTwo*10**9
            ans=self.twoDigits(firstTwo)+" Billion"
            remString=self.millions(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        elif(l==12):
            firstThree=digits[0]*100+digits[1]*10+digits[2]
            rem=n-firstThree*10**9
            ans=self.threeDigits(firstThree)+" Billion"
            remString=self.millions(rem)
            if(remString!=""):
                ans+=" "+remString
            return ans
        return ""
        
        
    def numberToWords(self, num: int) -> str:
        if(0<= num <10):
            #single digit
            return self.ones(num)
        elif(10<= num <100):
            return self.twoDigits(num)
        elif(100<=num<1000):
            return self.threeDigits(num)
        elif(1000<=num<1000000):
            return self.thousands(num)
        elif(1000000<=num<1000000000):
            return self.millions(num)
        else:
            return self.billions(num)
        
        
            
