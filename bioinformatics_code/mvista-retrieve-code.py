import sys

def submit_data(*fasta_files):
	
	"fasta_files is variable according to the input"

	# access the website wiht mechanize
	import mechanize
	import time

	#define a function a retrieve data from a website

	"use module mechanize to open a specific website,have to rewrite the website and submitted forms according to the website"

	#open an website
	br = mechanize.Browser()

	#ignore the robot.txt
	br.set_handle_robots(False)
	#User-Agent
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


	#open the website
	number = len(fasta_files)
	seq_number = str(number)
	website = 'http://genome.lbl.gov/cgi-bin/VistaInput?num_seqs=' + seq_number
	response = br.open(website)
	#print response.read()

	
	#check the number of forms
	print len(br.forms())

	for form in br.forms():
		print form.name
		print form
	

	#select forms to fill
	br.select_form("vform")

	#fill the email text
	br.form['email'] = "chencheng101023@163.com"
	time.sleep(1)

	#upload the sequence file
	i = 0
	for fasta_file in fasta_files :
		i = i+1	
		seq_name = 'seq'+str(i)
		sequence_name = 'name'+str(i) 
		print fasta_file
		br.form.add_file(open(fasta_file), 'text/plain', fasta_file, name = seq_name)
		time.sleep(1)
		br.form[sequence_name] = fasta_file.strip(".gff_plus_20k")
		time.sleep(2)
		#br.form.add_file(open("seahorse_sox9.gff_plus_20k"), 'text/plain', "seahorse", name = 'seq2')
		#time.sleep(1)


	newpage = br.submit()
	
print "submitting data to the mvista server, please check your email"

submit_data(*sys.argv[1:])

'''
#select specific forms to submit the data
br.select_form(nr = 0)


#fill the form with query protein amino acid sequence
br['3'] = str('f[key]')

#submit the form and save a new web page
newpage = br.submit()

#get the url for further action
url = newpage.geturl()

#time delay to get all the contents in the webpage
time.sleep(10) #use seconds as unit,and it's a tricky problem to set the time lapse

htmltext= br.open(url).read() #what is the function of timeout?
print htmltext


#looking for signal peptide
pattern = re.compile("SP='NO'")
found = re.search(pattern, htmltext)

if not found:

	#extract the information in each results
	#pattern = re.compile('P>\n(.*?)\n# <A', re.S) #multiline pattern, so use re.S
	#text = re.findall(pattern,htmltext)
	
	#save the retrieved data
	#f1 = open('signal_data.txt', 'a')
	#f1.write('>'+key+'\n'+text[0]+'\n')
	#f1.close()
	return 1



#INPUT FROM A GIVEN DATASET

# filter the suumitted sequence

f = Fasta('proteins.fasta') #pyfasta function
keys = sorted(f.keys())
for key in keys[0:2]:
	if submit(key):	
		#save the retrieved data
		f1 = open('signal_data.txt', 'a')
		f1.write('>'+key+'\n'+ f[key][:]+'\n')
		f1.close()

'''

