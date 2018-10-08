#given an alignment matrix and two protein sequences, output the best matched sequence

import sys

'''

Allow free taxi rides to the beginning of first string and from  end of second string ( row 0 and column 0 of alignment matrix will have zeroes) . Then use global alignment algorithm. To find sink node , search only along the bottom row of alignment matrix (in reverse sequence: last column to first) to find the highest  scoring node. That is the end of the overlap suffix in the second string. Then backtrack from that node until you hit column 0 to compute overlapping subsequences. Hope that helps.
'''

def OverMatch(v,w):
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


	for i in range(1,len(v)):
		s[i][0] = 0
		#backtrack[i][0]= "f" # f denotes free ride
	for j in range(1,len(w)):
		s[0][j]= -2*j
		#backtrack[0][j]="f"
	s[0][0] = 0	
	
	
	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			if v[i-1] == w[j-1]:
				s[i][j] = max(s[i-1][j]-2,s[i][j-1]-2,s[i-1][j-1]+1)
				if s[i][j] == s[i-1][j]-2:
					backtrack[i][j]= "v"  # v denotes vertical
				elif s[i][j] == s[i][j-1]-2:
					backtrack[i][j] = "h" #h denotes horizonal
				elif s[i][j]==s[i-1][j-1]+1:
					backtrack[i][j] = "d" # d diagonal
				
			else:
				s[i][j] = max(s[i-1][j]-2,s[i][j-1]-2, s[i-1][j-1]-2 )
				if s[i][j] == s[i-1][j]-2:
					backtrack[i][j]= "v"  # v denotes vertical
				elif s[i][j] == s[i][j-1]-2:
					backtrack[i][j] = "h" #h denotes horizonal
				elif s[i][j]==s[i-1][j-1]-2:
					backtrack[i][j] = "d" # d diagonal
	#looking for maximum score from the bottom column
	max_score = 0
	max_i = 0
	max_j = 0
	for j in range(0,len(w)+1):
		#print s[len(v)][j]
		if max_score <= s[len(v)][j]: #remain quesitions
			max_score = s[len(v)][j]
			max_j = j
	i = len(v)
	j = max_j # simplify denotation
	#print max_j
	seq1 = ""
	seq2 = ""
	while i>0 and j> 0:
		
		if backtrack[i][j]== "d":
			seq1 += v[i-1]
			seq2 += w[j-1]
			i = i-1
			j = j-1		
		elif backtrack[i][j] == "v":
			seq1 += v[i-1]
			i = i-1
			seq2 += "-"
		elif backtrack[i][j] == "h":
			seq2 += w[j-1]
			j = j-1
			seq1 += "-"
	return (max_score,seq1[::-1],seq2[::-1])



f = open(sys.argv[1], "r")
lines = f.readlines()
string1 = lines[0].strip()
string2 = lines[1].strip()
f.close()



#string1 = "GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA"
#string2 = "TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG"
overlap = OverMatch(string1, string2)


print overlap[0]
print overlap[1]
print overlap[2]


