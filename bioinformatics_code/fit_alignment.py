#given an alignment matrix and two protein sequences, output the best matched sequence

import sys


def FitAlignment(v,w):
	# v and w is a string
	#score matrix initialization
	s = []
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		s.append(tmp)

	backtrack = []	
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		backtrack.append(tmp)
	
	#score caculation for matches and backtrack, be careful with the bound and don't forget to caculate it
	for i in range(1,len(v)-len(w)+1):
		s[i][0] = 0
		backtrack[i][0]= "s" #from source
	#for i in range()
	for j in range(1,len(w)+1):
		s[0][j]= -j
		backtrack[0][j]="h"
	s[0][0] = 0	
	Match = 1
	indel = 1
	Mismatch = 1	

	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			if v[i-1] == w[j-1]:
				s[i][j] = max(s[i-1][j]-1,s[i][j-1]-1,s[i-1][j-1]+1)
				if s[i][j] == s[i-1][j]-1:
					backtrack[i][j]= "v"  # v denotes vertical
				elif s[i][j] == s[i][j-1]-1:
					backtrack[i][j] = "h" #h denotes horizonal
				elif s[i][j]==s[i-1][j-1]+1:
					backtrack[i][j] = "d" # d diagonal
				
			else:
				s[i][j] = max(s[i-1][j]-1,s[i][j-1]-1, s[i-1][j-1]-1)
				if s[i][j] == s[i-1][j]-1:
					backtrack[i][j]= "v"  # v denotes vertical
				elif s[i][j] == s[i][j-1]-1:
					backtrack[i][j] = "h" #h denotes horizonal
				elif s[i][j]==s[i-1][j-1]-1:
					backtrack[i][j] = "d" # d diagonal
	
	max_score = 0
	max_i = 0
	max_j = len(w)
	for i in range(1,len(v)+1):
		if max_score < s[i][j]:
			max_score = s[i][j]
			max_i = i
	
	seq1 = ""
	seq2 = ""
	i = max_i
	j = max_j
	while i >= 0 and j >= 0:
		if backtrack[i][j]== "d":
			seq1 += v[i-1]
			seq2 += w[j-1]
			i = i-1
			j = j-1
			
		elif backtrack[i][j] == "v":
			
			seq1 += v[i-1]
			seq2 += "-"
			i = i-1
			
		elif backtrack[i][j]=="h":
			seq1 += "-"
			seq2 += w[j-1]
			j = j-1
		else:
			break #get out of the cycle when i=j=0, since backtrack[0][0] is no sense
			
	return (max_score,seq1[::-1],seq2[::-1])
'''
f = open(sys.argv[1], "r")
lines = f.readlines()
v= lines[0].strip()
w= lines[1].strip()
f.close()
'''


v="GTTGGATTACGAATCGATATCTGTTTG"
w="ACGTCG"
match = FitAlignment(v,w)

print match[0]
print match[1]
print match[2]

