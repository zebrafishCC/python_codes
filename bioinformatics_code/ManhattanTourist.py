f = open("input.txt","r")
lines = f.readlines()
dimensions = lines[0].strip().split()
n = int(dimensions[0])
m = int(dimensions[1])
down = []
right = []

for i in range(1,n+1):
	weights = lines[i].strip().split()
	down.append(weights)
	
for j in range(n+2,n+2+n+1):
	weights = lines[j].strip().split()
	right.append(weights)

#print right

f.close()

def ManhattanTourist(n,m,down,right):
	
	#n,m represents the dimension of nodes, down and right are matrix weight
	#matrix initialization
	s = []
	for i in range(0, n+1):
		tmp = []
		for j in range(0,m+1):
			tmp.append(0)
		s.append(tmp)
	
	#handle the first row and first column
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + int(down[i-1][0])
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + int(right[0][j-1])
	
	#calculate s[i][j] using dynamic programming
	for i in range(1,n+1):
		for j in range(1,m+1):
			down_move = s[i-1][j]+int(down[i-1][j])
			right_move = s[i][j-1]+int(right[i][j-1])
			if down_move > right_move:
				s[i][j] = down_move
			else:
				s[i][j] = right_move
	return s[n][m]

#n = 4
#m = 4
#down = [[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]]
#right = [[3,2,4,0],[3,2,4,2],[0,7,3,3],[3,3,0,2],[1,3,2,2]]

print ManhattanTourist(n,m,down,right)


