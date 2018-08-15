#https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s):
     
        n=len(s)
        info={'I':1,'V':5,'X':10,'C':100,'L':50,'D':500,'M':1000}
        additional={'IV':4,'IX':9,'CM':900,'CD':400,'XL':40,'XC':90}
        ans=0
        for i in range(n):
            c=s[i]
            
            if(i!=0 and (c=='V' or c=='X') and s[i-1]=='I'):
                    ans+=additional[s[i-1]+s[i]]
                    ans-=1
            elif(i!=0 and (c=='M' or c=='D')and s[i-1]=='C'):
                    
                    ans+=additional[s[i-1]+s[i]]
                    ans-=100
            elif(i!=0 and (c=='C' or c=='L')and s[i-1]=='X'):
                 
                    ans+=additional[s[i-1]+s[i]]
                    ans-=10
            
            else:
                
                ans+=info[c]
        
        return ans
            
