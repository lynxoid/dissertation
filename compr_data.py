# gzip, bzip, plzip
seq_data = ["SRR635193\_1 & 448028499 & 388127969 & 298812728 \\",
"SRR519063\_1 & 275904124 & 171751232 & 149554794 \\",
"ERR233214\_1 & 208082597 & 189126709 & 119758802 \\"]


names = []
for l in seq_data:
	parts = l.strip(" \\").split(" & ")
	names.append(parts[0])
	# print parts
	megabytes = []
	for i in xrange(1, len(parts)):
		p = parts[i]
		megabytes.append( int( int(p.strip()) / 1024.0 /1024) )
	# print megabytes
	print "{} & {} \\\\".format( parts[0], " & ".join( map(str, megabytes) ) )

########################################################################
print "Ordered reads"

# gzip, bzip, plzip
ordered_data = ["175016102 & 205488130 & 134708764 \\",
"45838628 & 51280597 & 29998694 \\",
"99645423 & 127079363 & 67749051 \\"
]

for j, l in enumerate(ordered_data):
	parts = l.strip(" \\").split(" & ")
	# print parts
	megabytes = []
	for i in xrange(len(parts)):
		p = parts[i]
		megabytes.append( int( int(p.strip()) / 1024.0 /1024) )
	# print megabytes
	print "{} & {} \\\\".format( names[j], " & ".join( map(str, megabytes) ) )
