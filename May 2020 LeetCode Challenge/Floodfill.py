#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        sourceColor=image[sr][sc]
        visited=[[False for j in range(m)]for i in range(n)]
        def dfs(i,j):
            if(image[i][j]!=sourceColor):
                #not the same as source color
                return
            
            visited[i][j]=True #mark visited
            image[i][j]=newColor #fill color!
           
            #visit 4 directions
            if(i+1<n and not visited[i+1][j]):
                dfs(i+1,j)
            if(i-1>=0 and not visited[i-1][j]):
                dfs(i-1,j)
            if(j+1<m and not visited[i][j+1]):
                dfs(i,j+1)
            if(j-1>=0 and not visited[i][j-1]):
                dfs(i,j-1)
            
        dfs(sr,sc)
        return image
        