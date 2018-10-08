f = open("test.txt","r")
lines = f.readlines()
source = lines[0].strip()
sink = lines[1].strip()

graph = []  #graph matrix
for i in range(0, int(sink)+1):
	tmp = []
	for j in range(0,int(sink)+1):
		tmp.append(0)
	graph.append(tmp)

for line in lines[2:]:
	line = line.strip()
	weight = int(line.split(":")[1])
	start_node = int(line.split(":")[0].split("->")[0])
	end_node = int(line.split(":")[0].split("->")[1])
	graph[start_node][end_node] = weight

def toposort(graph):
	indegree = {}
	for node in range(0,len(graph)):
		indegree[node] = 0  
	for start in range(0,len(graph)):
		for end in range(0,len(graph)):
			if graph[start][end] > 0:
				indegree[end] += 1
	Q = [u for u in range(0,len(graph)) if indegree[u]==0]
	seq = []
	while Q:
		u = Q.pop()
		seq.append(u)
		for end in range(0,len(graph)):
			if graph[u][end]>0:
				indegree[end] -= 1
				if indegree[end] == 0:
					Q.append(end)
	if len(seq) == len(graph):
		return seq
	else:
		print "circle exists in the graph"

#print toposort(graph)

def LongestPath(graph, source, sink):
	s = []
	for node in range(0,len(graph)):
		s.append(-100000) #for initialization
	s[source] = 0
	topo_sort = toposort(graph)
	for i in range(len(topo_sort)):
		if topo_sort[i] == source:
			source_index = i
		if topo_sort[i] == sink:
			sink_index = i
	
	
	path = {}

	for endnode in topo_sort[source_index+1:sink_index+1]:
		max_path = 0
		for startnode in topo_sort[source_index:sink_index+1]:		
			if graph[startnode][endnode] > 0: #topological sorting have removed end to start edge
				#print startnode,endnode
				if max_path < s[startnode]+graph[startnode][endnode]: #should reset max_path for every cycle
					max_path = s[startnode]+graph[startnode][endnode]
					path[endnode] = startnode
					
		s[endnode] = max_path
	return (s[sink],path)

#print source,sink

longestpath = LongestPath(graph, int(source), int(sink))
pathlength = longestpath[0]
print pathlength

pathdict = longestpath[1]
#print pathdict

reversepath = []
sink = int(sink)
#reverse_path.append(sink)
while sink != int(source):
	reversepath.append(str(sink))
	sink = pathdict[sink]
reversepath.append(source)
truepath = reversepath[::-1]
print "->".join(truepath)


		
