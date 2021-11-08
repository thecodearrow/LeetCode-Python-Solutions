class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        #construct isPali matrix
        isPali=[[False for j in range(n)] for i in range(n)]
        for l in range(n):
            for i in range(n-l):
                j=i+l
                if(i==j):
                    isPali[i][j]=True
                else:
                    if(s[i]==s[j]):
                        if(l==1):
                            isPali[i][j]=True
                        else:
                            isPali[i][j]=isPali[i+1][j-1]
                    else:
                        isPali[i][j]=False
                        
        #count the number of occurrences in matrix
        ans=0
        for i in range(n):
            for j in range(n):
                if(isPali[i][j]):
                    ans+=1
        
        #you can optimise this further to count while updating the matrix itself! :)
        return ans
