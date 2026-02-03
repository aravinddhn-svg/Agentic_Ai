### shorest dist and  path:


import heapq



def short_dis(s,e,graph):

	pq=[(0,s)] ## staring node

	visited = set() ## avoid duplicate reprocess on main nodes not neigh

	dis={ node:float("inf") for node in graph}

	dis[s]=0

	parent={} ## to keep the path 

	while pq:

		curr_dis,node=heapq.heappop(pq)

		if node in visited:
			continue

		visited.add(node)

		if node==e:
			break

		for neigh,w in graph[node].items():
			new_dis=curr_dis+w
			if new_dis <dis[neigh]:
				dis[neigh]=new_dis
				parent[neigh]=node ## store parent of all the child nodes
				heapq.heappush(pq,(new_dis,neigh))
	path=[]
	curr=e ## create path from the end node

	while curr !=s:
	    path.append(curr)
	    curr=parent[curr]	## get the parent of curr node
	path.append(s)    
	path.reverse()    
	return path,dis[e]    				

s="a"
e="d"

graph={
	'a':{'b':2,'c':5},
	'b':{'d':15,'e':1},
	'c':{"d":10},
	'e':{'d':3},
	'd':{}

}

dis=short_dis(s,e,graph)
