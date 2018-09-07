import sys

gtf=open(sys.argv[1])

gidlst=[]
trcidlst=[]
while True:
	line = gtf.readline()
	if not line:
		break
	spt = line.split('\t')
	spc = spt[-1].split(';')
	geneid=spc[0].split('"')[1]
	transcriptid=spc[1].split('"')[1]
	if not(geneid in gidlst):
		gidlst.append(geneid)
	if not(transcriptid in trcidlst):
		trcidlst.append(transcriptid)
#make Not overlap gene_id, transcript_id list
geneidcount = len(gidlst)
trcidcount = len(trcidlst)

print('gene_id의 총 개수는 : ',geneidcount,' transcript_id의 총 개수는 : ',trcidcount)

gtf.close()