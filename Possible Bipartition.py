#https://leetcode.com/contest/weekly-contest-97/problems/possible-bipartition/

"""

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.


"""

#Make a graph using the dislike edges and check if it is 2-colorable


from collections import defaultdict 

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)


	def addEdges(self,u,v):
		self.neighbours[u].append(v)
		self.neighbours[v].append(u)

	def check2colorable(self):
		s=1
		visited=defaultdict(lambda:False)
		visited[s]=True
		color={}
		color[s]=0 
		queue=[s]
		while queue:
			u=queue.pop(0)
			for v in self.neighbours[u]:
				if(v in visited):
					if(color[v]==color[u]):
						return False 
				if(v not in visited):
					visited[v]=True 
					color[v]=1-color[u]
					queue.append(v)

		return True 


class Solution:
	def possibleBipartition(self, N, dislikes):
		g=Graph()
		for d in dislikes:
			u,v=d[0],d[1]
			g.addEdges(u,v)

		return g.check2colorable()