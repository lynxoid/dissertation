data = '''	SRR037452	SRR1294122	SRR527697	SRR553460	SRR553463	SRR034940_1
SRR037452	1.000	0.040	0.003	0.061	0.058	0.006
SRR1294122	0.040	1.000	0.005	0.077	0.075	0.028
SRR527697	0.003	0.005	1.000	0.005	0.005	0.002
SRR553460	0.061	0.077	0.005	1.000	0.270	0.028
SRR553463	0.058	0.075	0.005	0.270	1.000	0.030
SRR034940_1	0.006	0.028	0.002	0.028	0.030	1.000'''

lines = data.split("\n")
print len(lines)
header = lines[0].split("\t")
print " {} \\\\".format( " & ".join(header) )

for line in lines[1:]:
	parts = line.split('\t')
	print "{} \\\\".format( " & ".join(parts) )