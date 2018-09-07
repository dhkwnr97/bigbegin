#input_gtf_file(/spbar)result_fileout_directory[like:/home/hanjg/]
import sys

input_gtf=open(sys.argv[1],'r')
input_fileName=sys.argv.split('/')[-1]
result=open(sys.argv[2]+input_fileName+'_CountResult.txt','w')

trc_Ndic={}
exonCount=0
while True:
	oneL=input_gtf.readline()
	
	if not oneL:
		break#end of file, must break
	
	spt=oneL.split('\t')
	if spt[2] == 'transcript':
		if not has_key(str(exonCount)):
			trc_Ndic[str(exonCount)]=1
		else:
			trc_Ndic[str(exonCount)]+=1
		exonCount=0
	else:#when line is exon line
		exonCount+=1
################################
if not has_key(str(exonCount)):
	trc_Ndic[str(exonCount)]=1
else:
	trc_Ndic[str(exonCount)]+=1
#for the last transcript
#################################
'''
we make dictionary like:{'1':12341, '2':123, '3':21, ...}
mean = in gtf, 
Number of single exon transcript : 12341 / 
Number of two exon transcript : 123 /
Number of three exon transcript : 21
...and so on
'''
result.write('N_exon_transcript'+'\t'+'number_of_trc')
for key in trc_Ndic:
	result.write(key+'\t'+trc_Ndic[key])

input_gtf.close()
result.close()