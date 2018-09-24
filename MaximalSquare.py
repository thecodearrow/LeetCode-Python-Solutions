#https://leetcode.com/problems/maximal-square/description/

#https://www.youtube.com/watch?v=NYeVhmWsWec&t=721s

class Solution:
    def maximalSquare(self, matrix):
        if(matrix==[]):
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        
        dp=[]
        ans=0 
        for i in range(rows):
            dp.append([])
            for j in range(cols):
                dp[i].append(0)
                
        for i in range(cols):
            if(matrix[0][i]=="1"):
                dp[0][i]=1 
                ans=1
        
        for j in range(rows):
            if(matrix[j][0]=="1"):
                dp[j][0]=1
                ans=1
                
              
        for i in range(1,rows):
            for j in range(1,cols):
                if(matrix[i][j]=="1"):
                    size=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                    dp[i][j]=size+1
                    ans=max(dp[i][j],ans)
       
        area=ans*ans
        return area
                    
        