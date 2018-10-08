f = open("test.txt","r")
lines = f.readlines()
source = lines[0].strip()
sink = lines[1].strip()

'''
sample dataset

4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6

'''

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


