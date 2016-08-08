import sys                # bring in a standard library 
lines = sys.__stdin__.readlines() # read every line from stdin into an array! 

lines = [x.strip() for x in lines]

end_nodes = []
start_nodes = []

unalt_end = []
unalt_start = []

it = iter(lines)
edges = zip(it, it)

for (a,b) in edges:
	unalt_end.append(a)
	unalt_start.append(b)

new_edges = []

for edge in edges:
	edge = list(edge)
	edge.insert(1, ord(edge[1][0]))
	edge = tuple(edge)
	new_edges.append(edge)

for edge in new_edges:
	end_nodes.append(edge[0])
	start_nodes.append(edge[2])

L = []
S = []

for node in start_nodes:
	if node not in end_nodes and node not in S:
		S.append(node)

while S != []:
	S.sort()
	n = S.pop(0)
	L.append(n)
	for edge in edges[:]:
		if edge[1] == n:
			edges.remove(edge)
			unalt_end.remove(edge[0])
			if edge[0] not in unalt_end:
				S.insert(0, edge[0])

if edges != []:
	print "cycle"

else:
	for l in L:
		print l


