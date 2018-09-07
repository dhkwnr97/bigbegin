import sys

tracfile=open(sys.argv[1])

i=0
j=0
while True:
	line = gtf.readline()
	if not line:
		break
	spt = line.split('\t')
	if spt[3] == 'u':
		i=i+1
	if spt[3] == 'x':
		j=j+1

print(i,j)

tracfile.close()