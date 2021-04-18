#O(n*m^2 ) solution
#https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3711/

class Solution:

    def computePrefixSum(self,matrix,n,m):
        prefix=[row[:] for row in matrix] #copy matrix
        #rowwise
        for i in range(1,n):
            for j in range(m):
                prefix[i][j]+=prefix[i-1][j]
        #colwise
        for i in range(n):
            for j in range(1,m):
                prefix[i][j]+=prefix[i][j-1]
        #print(prefix)
        return prefix
    
    def computeSubmatrixSum(self,x1,y1,x2,y2,prefix):
        #compute submatrix sum using prefixsum
        whole=prefix[x2][y2]
        top=prefix[x1-1][y2] if x1>=1 else 0
        left=prefix[x2][y1-1] if y1>=1 else 0
        common=prefix[x1-1][y1-1] if (x1>=1 and y1>=1) else 0
        return whole-top-left+common
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        prefix=self.computePrefixSum(matrix,n,m) #0,0 to i,j sum precompute
        ans=0
        for x1 in range(n):
            for y1 in range(m):
                for x2 in range(x1,n):
                    for y2 in range(y1,m):
                        #print(x1,y1,x2,y2)
                        currentSum=self.computeSubmatrixSum(x1,y1,x2,y2,prefix)
                        if(currentSum==target):
                            ans+=1
        
    
        return ans
                                
                        