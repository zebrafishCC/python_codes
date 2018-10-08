#given two strings, output the edit distance between two strings
import sys

def EditDistance(v,w):
	# v and w is a string
	#score matrix initialization
	s = []
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		s.append(tmp)

	#backtranck matrix intialization, every backstrack match a score, except backtrack[0][0]
	backtrack = []	
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		backtrack.append(tmp)
	
	#score caculation for matches and backtrack, be careful with the bound and don't forget to caculate it
	for i in range(1,len(v)+1):
		s[i][0] = i
		backtrack[i][0]= "v"
	for j in range(1,len(w)+1):
		s[0][j]= i
		backtrack[0][j]="h"
	s[0][0] = 0	
	
	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			if v[i-1] == w[j-1]:
				s[i][j] = s[i-1][j-1]
			else:
				s[i][j] = min(s[i-1][j]+1,s[i][j-1]+1,s[i-1][j-1]+1)

			if s[i][j] == s[i-1][j]+1:
				backtrack[i][j]= "v"  # v denotes vertical,delete
			elif s[i][j] == s[i][j-1]+1:
				backtrack[i][j] = "h" #h denotes horizonal,insert
			elif s[i][j]==s[i-1][j-1]+1:
				backtrack[i][j] = "s" # s denotes substitute
			else: 
				backtrack[i][j] = "m" #m denotes match
	min_score=s[len(v)][len(w)]
	
	return min_score

f = open(sys.argv[1], "r")
lines = f.readlines()
v= lines[0].strip()
w= lines[1].strip()
f.close()

match = EditDistance(v,w)


print match


