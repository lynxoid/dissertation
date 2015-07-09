data = '''	Cell type	Read count/len	shared with T	unique to file	unique to T
SRR037452	MAQC brain tissue	13,552,276/ 35	18,513,744	59,214,972	94,883,622
SRR1294122	ES	39,666,314/101	58,694,264	408,807,236	54,703,102
SRR034940	WGS, random cell	72,795,628/100	28,697,479	916,749,539	84,699,887
SRR553463*	neutrophil	49,771,919/ 49	34,291,992	118,624,324	79,105,374
SRR553460*	neutrophil	66,552,453/ 49	35,242,903	119,608,311	78,154,463
SRR527697	placenta, ENCODE	169,606,661/101	2,053,392	246,196,849	111,343,974
SRR445718	oocyte (embryo)	32,943,665/101	32,051,874	246,196,849	81,345,492'''

lines = data.split("\n")
print len(lines)
header = lines[0]
column_names = header.split('\t')
print len(column_names)
print "* {} \\\\".format( " & ".join(column_names) )
data_names = []

for line in lines[1:]:
	ps = line.split('\t')
	data_name = ps[0]
	type = ps[1]
	print "{}\t& {} & {} \\\\".format(data_name, type, " & ".join( [ "".join(p.split(",")) for p in ps[2:]] ) )