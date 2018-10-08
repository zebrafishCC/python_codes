#give different penalties for gap open and gap extension

'''
Code Challenge: Solve the Alignment with Affine Gap Penalties Problem.
     Input: Two amino acid strings v and w (each of length at most 100).
     Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score. Use the
     BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.

Download BLOSUM62 scoring matrix

Extra Dataset
'''
#BLOSUM62

matrix = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

#indel penalty
gap_open = 11
gap_extension = 1

def AffineAlignment(v,w,matrix):
	# v and w is a string
	#score matrix initialization, build lower (represents insertion), middle(match or mismatch) and upper (deletion) matrixes
	lower = []
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		lower.append(tmp)

	middle = []
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		middle.append(tmp)
	
	upper = []
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		upper.append(tmp)

	#backtranck matrix intialization, every backstrack match a score, except backtrack[0][0]
	backtrack = []	
	for i in range(0,len(v)+1):
		tmp = []
		for j in range(0,len(w)+1):
			tmp.append(0)
		backtrack.append(tmp)

	#score matrix initialization
	lower[0][0] = 0
	lower[1][0] = -gap_open
	backtrack[1][0] = "v"
	for i in range(2,len(v)+1):
		lower[i][0] = -gap_extension*(i-1)-gap_open
		backtrack[i][0]= "v"		
					
	
	upper[0][0] = 0
	upper[0][1] = -gap_open
	backtrack[0][1] = "h"
	for j in range(2,len(w)+1):
		upper[0][j]= -gap_extension*(i-1)-gap_open
		backtrack[0][j]="h"
	for i in range(1,len(v)+1):
		upper[i][0] = lower[i][0]

	for j in range(1, len(w)+1):
		lower[0][j] = upper[0][j] #not allowed horizontal move in lower matrix

	middle[0][0] = 0	
	for i in range(1,len(v)+1):
		middle[i][0] = lower[i][0]
	for j in range(1, len(w)+1):
		lower[0][j] = upper[0][j]

	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):	
			lower[i][j] = max(lower[i-1][j]-gap_extension, middle[i-1][j]-gap_open)
			upper[i][j] = max(upper[i][j-1]-gap_extension, middle[i][j-1]-gap_open)
			middle[i][j] = max(lower[i][j],middle[i-1][j-1]+matrix[v[i-1]][w[j-1]], upper[i][j])
			if middle[i][j] == lower[i][j]:
				backtrack[i][j] = "v"
			elif middle[i][j] == upper[i][j]:
				backtrack[i][j] = "h"
			elif middle[i][j] == middle[i-1][j-1]+matrix[v[i-1]][w[j-1]]:
				backtrack[i][j] = "d"
			else:
				continue
			lower[i][j] = middle[i][j]
			upper[i][j] = middle[i][j]
			print middle[i][j]
	
	
	i = len(v)
	j = len(w)
	max_score = middle[i][j]
	
	seq1 = ""
	seq2 = ""
	while i > 0 and j > 0:
		if backtrack[i][j]=="d"	:
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
	return (max_score,seq1[::-1],seq2[::-1])
'''
f = open(sys.argv[1], "r")
lines = f.readlines()
v= lines[0].strip()
w= lines[1].strip()
f.close()

'''
v = "PRTEINS"
w = "PRTWPSEIN"

match = AffineAlignment(v,w,matrix)

print match[0]
print match[1]
print match[2]
