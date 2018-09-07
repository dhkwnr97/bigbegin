#input_gtf_file(/spbar)result_fileout_directory[like:/home/hanjg/]
import sys

input_gtf=open(sys.argv[1],'r')
input_fileName=sys.argv.split('/')[-1]
result=open(sys.argv[2]+input_fileName+'_trcLengthResult.txt','w')

trc_Legdic={}
trcleng=0
trcid=''
while True:
	oneL=input_gtf.readline()
	
	if not oneL:
		break#end of file, must break
	
	spt=oneL.split('\t')
	if spt[2] == 'transcript':
		result.write(trcid+'\t'+trcleng)
		trcid=oneL.split('"')[3]#analyzing new transcript
		trcleng=0#initialization transcript length
	else:#if that line is exon line.
		if oneL.split('"')[3] == trcid:
			trcleng+=(int(spt[4])-int(spt[3])+1)

################################
result.write(trcid+'\t'+trcleng)
#for the last transcript
################################

input_gtf.close()
result.close()