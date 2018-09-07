import sys

def serch(trcfile):
        ux_gtnlst = []
        while True:
                trc_oneline = trcfile.readline()
                if not trc_oneline:
                        break
                noent = trc_oneline.strip('\n')
                sptab = noent.split('\t')
                if sptab[3] == 'u' or sptab[3] == 'x':
                        spbar = (sptab[-1]).split('|')
                        ux_gtnlst.append(spbar[0][3:]+'-'+spbar[1])

        return ux_gtnlst

def findNwrite(cufcomfile, ux_gtnlst):
        while True:
                cufcom_oneline = cufcomfile.readline()
                if not cufcom_oneline:
                        break
                noent = cufcom_oneline.strip('\n')
                sptab = noent.split('\t')
                if len(sptab) > 2:
                        spscol = sptab[8].split(';')
                        matchcheck = (spscol[0].split('"'))[1]+'-'+(spscol[1].split('"'))[1]
                        if matchcheck in ux_gtnlst:
                                newf.write(cufcom_oneline)

trckf = open(sys.argv[1],'r')
cufcom_gtf = open(sys.argv[2],'r')
newf = open('/home/hanjg/cufcom_u_x.gtf','w')

sch_trck = serch(trckf)
findNwrite(cufcom_gtf, sch_trck)

trckf.close()
cufcom_gtf.close()
newf.close()