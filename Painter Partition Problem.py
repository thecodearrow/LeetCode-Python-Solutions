#https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0/?track=placement

#https://articles.leetcode.com/the-painters-partition-problem-part-ii/

"""
Beautiful DP problem that can be solved in O(k*N^2) :) 
"""

t=int(input())
while t!=0:
	t-=1
	k,n=[int(x) for x in input().split()]
	a=[int(x) for x in input().split()]
	dp=[]

	for i in range(k):
		dp.append([])
		for j in range(n):
			dp[i].append(0)

	start=0
	for i in range(n):
		start+=a[i]
		dp[0][i]=start 
	
	for w in range(1,k):
		for i in range(n):
			minimum_sum=dp[0][i] #prefix sum till i 
			suffix=0
			for j in range(i,0,-1): #i to 1 backwards
				minimum_sum=min(max(a[j]+suffix,dp[w-1][j-1]),minimum_sum)
				suffix+=a[j]
			dp[w][i]=minimum_sum

	print(dp[k-1][n-1])