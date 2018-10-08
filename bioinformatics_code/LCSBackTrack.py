

#f = open(test.txt)




def LCSBackTrack(v,w):
	# v and w is a string
	#score matrix initialization
	s = []
	for i in range(0,len(v)):
		tmp = []
		for j in range(0,len(w)):
			tmp.append(0)
		s.append(tmp)

	#backtranck matrix intialization
	BackTrack = []	
	for i in range(0,len(v)):
		tmp = []
		for j in range(0,len(w)):
			tmp.append(0)
		BackTrack.append(tmp)
	
	#score caculation for matches and backtrack, be careful with the bound and don't forget to caculate it
	for i in range(0,len(v)):
		s[i][0] = 0
		BackTrack[i][0]= "v"
	for j in range(0,len(w)):
		s[0][j]= 0
		BackTrack[0][j]="h"
	if v[0]==w[0]:
		s[0][0] = 1
		BackTrack[0][0] = "d"
	for i in range(1,len(v)):
		for j in range(1,len(w)):
			if v[i]==w[j]:
				temp=s[i-1][j-1]+1
				s[i][j] = max(s[i-1][j],s[i][j-1],temp)
			else:
				s[i][j] = max(s[i-1][j],s[i][j-1])
			if s[i][j] == s[i-1][j]:
				BackTrack[i][j]= "v"  # v denotes vertical
			elif s[i][j] == s[i][j-1]:
				BackTrack[i][j] = "h" #h denotes horizonal
			elif s[i][j]==s[i-1][j-1]+1 and v[i]==w[j]:
				BackTrack[i][j] = "d" # d diagonal
	#print BackTrack
	return BackTrack

def OutputLCS(backtrack,v,i,j):
	"""	
	if i+1 == 0 or j+1 == 0:
		return None
	elif backtrack[i][j] == "v":
		OutputLCS(backtrack,v,i-1,j)
	elif backtrack[i][j] == "h":
		OutputLCS(backtrack,v,i,j-1)
	else:
		OutputLCS(backtrack,v,i-1,j-1)
		return v[i]
	"""
	lcs = ""
	while i >= 0 and j >= 0:
		if backtrack[i][j]=="d"	:
			lcs += v[i]
			i = i-1
			j = j-1
		elif backtrack[i][j] == "v":
			i = i-1
		else:
			j = j-1
	return lcs[::-1]
v = "TGTACG"
w= "GCTAGT"

backtrack = LCSBackTrack(v,w)
lcs = OutputLCS(backtrack,v,len(v)-1,len(w)-1)

print lcs
