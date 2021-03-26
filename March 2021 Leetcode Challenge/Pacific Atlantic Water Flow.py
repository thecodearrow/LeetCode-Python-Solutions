#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3684/

#Just calculate the intersection of Atlantic and Pacific!

class Solution:
    
    def valid(self,i,j,m,n):
        if(i<0 or j<0 or i>=n or j>=m):
            return False
        return True
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        
        if(n==0):
            return []
        m=len(matrix[0])
        queue_p=[]
        queue_a=[]
        directions=[(0, 1), (1, 0), (-1, 0), (0, -1)]
        pacific=[[False for j in range(m)] for i in range(n)]
        atlantic=[[False for j in range(m)] for i in range(n)]
        visited_a=[[False for j in range(m)] for i in range(n)]
        visited_p=[[False for j in range(m)] for i in range(n)]
        for i in range(n):
            queue_p.append((i,0))
            queue_a.append((i,m-1))
        
        
        for j in range(m):
            queue_p.append((0,j))
            queue_a.append((n-1,j))
        
        #BFS1
        while queue_p:
            i,j=queue_p.pop(0)
            pacific[i][j]=True
            for di,dj in directions:
                inew,jnew=i+di,j+dj
                if(self.valid(inew,jnew,m,n) and not visited_p[inew][jnew]):
                    if(matrix[inew][jnew]>=matrix[i][j]):
                        #can flow
                        queue_p.append((inew,jnew))
                        visited_p[inew][jnew]=True
        #BFS2
        while queue_a:
            i,j=queue_a.pop(0)
            atlantic[i][j]=True
            for di,dj in directions:
                inew,jnew=i+di,j+dj
                if(self.valid(inew,jnew,m,n) and not visited_a[inew][jnew]):
                    if(matrix[inew][jnew]>=matrix[i][j]):
                        #can flow
                        queue_a.append((inew,jnew))
                        visited_a[inew][jnew]=True
                        
        
        ans=[]
        
        for i in range(n):
            for j in range(m):
                if(pacific[i][j] and atlantic[i][j]):
                    ans.append([i,j])
        
        return ans
        
        
        
            
        
        