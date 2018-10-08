import mechanize

br = mechanize.Browser()

response = br.open("www.google.com")

for f in br.forms():
	print f


