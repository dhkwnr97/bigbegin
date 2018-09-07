#enter the gtf and filter Number.
import sys

gtf=open(sys.argv[1],'r')#input gtf file.
newname=gtf.replace('.gtf','_over_trc'+char(sys.argv[2])+'leng.gtf')
filtered_file=open(newname,'w')#filtered result file

overN=int(sys.argv[2])
imsi_lines=[]
imsi_sum=0
imsi_trcid=''

lines=gtf.readlines()
for each_line in lines:
	sptline=each_line.split('\t')
	if sptline[2] == 'transcript':#type is transcript
		if imsi_sum >= overN:
			for l in imsi_lines:
				filtered_file.write(l)
			imsi_lines=[]
			imsi_sum=0
			imsi_trcid=''
			#write whole correct things and initialization for other trc checking
		else:
			imsi_lines=[]
			imsi_sum=0
			imsi_trcid=''			
			#not correct given condition, just initialization for other trc checking
		imsi_lines.append(each_line)
		imsi_trcid=sptline[-1].split('transcript_id')[1].split('"')[1]#find line`s transcript_id
	else:#Not transcript info, it`s exon
		if sptline[-1].split('transcript_id')[1].split('"')[1] == imsi_trcid:#checking exon in same transcript
			imsi_lines.append(each_line)
			imsi_sum=imsi_sum+(int(sptline[4])-int(sptline[3]))

gtf.close()
filtered_file.close()