import sys

newfile=open('/home/hanjg/ref_1kb_cut_mrg4.gtf','w')

def mkrefdic(refgtf):
        reftrdic={}
        while True:
                line = refgtf.readline()
                if not line:
                        break
                spt = line.split('\t')
                spsmc = spt[-1].split('"')
                if spt[2] == 'exon':
                        keyname = str(spt[0]+'/'+spt[6]+'/'+spsmc[1])
                        if reftrdic.has_key(keyname):
                                reftrdic[keyname][1]=int(spt[4])
                        else:
                                reftrdic[keyname]=[int(spt[3]),int(spt[4]),str(spt[0]+'/'+spt[6])]
        return reftrdic         

def mkdicdarkzone(refdic):
        for i in refdic:
                mindz = int(refdic[i][0])-1000
                maxdz = int(refdic[i][1])+1000
                refdic[i].insert(2,maxdz)
                refdic[i].insert(0,mindz)
        return refdic

refgtf_f = open(sys.argv[1],'r')
refdic = mkrefdic(refgtf_f)
refdic_indz = mkdicdarkzone(refdic)
mrggtf_f = open(sys.argv[2],'r')

checkid=[]
while True:
        checktrc=[]
        line = mrggtf_f.readline()
        
        if not line:
                break
        #end signal
        spt = line.split('\t')
        
        if len(spt)<3:
                continue
        #just error shield
        spsmc = spt[-1].split('"')
        onelmax = int(spt[4])
        onelmin = int(spt[3])
        chrid_drtion = spt[0]+'/'+spt[6]
        if spt[2] == 'transcript':
                for i in refdic_indz:
                        if chrid_drtion == refdic_indz[i][4]:
                                if onelmax < refdic_indz[i][0] or onelmin > refdic_indz[i][3]:
                                        checktrc.append('+')
                                else:
                                        checktrc.append('-')            
                if '-' not in checktrc:
                        newfile.write(line)
                        checkid.append(spsmc[3])
        else:
                if spsmc[3] in checkid:
                        newfile.write(line)

refgtf_f.close()
mrggtf_f.close()
newfile.close()