import sys

gtf = open(sys.argv[1],'r')
cut1_m_gtf = open('/home/hanjg/cufcom_u_x_no1exon.gtf','w')

imsi=[]
while True:
	line = gtf.readline()
	if not line:
		break
	if line.split('\t')[2] == 'transcript':
		if len(imsi) > 2:
			for i in imsi:
				cut1_m_gtf.write()
		imsi=[]
		imsi.append(line)
	else:
		imsi.append(line)

gtf.close()
cut1_m_gtf.close()